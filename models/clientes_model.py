import pandas as pd
import numpy as np
from utils.db_conn import CSVClientesDB, CSVComprasDB

class ClientesModel:
    def __init__(self, db_clientes_path='data/clientes.csv', db_compras_path='data/compras.csv'):
        
        self.db_clientes = CSVClientesDB(path = db_clientes_path)
        self.df_clientes = None
        if self.db_clientes.verificar_csv():
            self.df_clientes = self.db_clientes.leer_csv()
        else:
            print("ADVERTENCIA: No se pudo cargar 'clientes.csv'")

        self.db_compras = CSVComprasDB(path = db_compras_path)
        self.df_compras = None
        if self.db_compras.verificar_csv():
            self.df_compras = self.db_compras.leer_csv()
            if self.df_compras is not None and 'fecha' in self.df_compras.columns:
                if not pd.api.types.is_datetime64_any_dtype(self.df_compras['fecha']):
                    self.df_compras['fecha'] = pd.to_datetime(self.df_compras['fecha'], errors='coerce')
                    self.df_compras = self.df_compras.dropna(subset=['fecha'])
        else:
            print("ADVERTENCIA: No se pudo cargar 'compras.csv'")

    def get_clientes_unicos(self):
        if self.df_clientes is None:
            print("Error: No se pudo acceder a la lista de clientes.")
            return []
        try:
            clientes = sorted(list(self.df_clientes['nombre'].unique()))
            return clientes
        except KeyError:
            print("Error: Columna 'nombre' no encontrada en 'clientes.csv'.")
            return []

    def get_reporte_clientes_activos(self, top_n=3):
        if self.df_compras is None or self.df_clientes is None:
            print("Error: Faltan datos de compras o clientes para generar el reporte.")
            return pd.DataFrame(columns=['nombre', 'Numero de Compras'])

        try:
            reporte_series = self.df_compras['cliente_id'].value_counts()
            
            reporte_top = reporte_series.head(top_n)
            
            df_reporte = reporte_top.reset_index()
            df_reporte.columns = ['cliente_id', 'Numero de Compras']
            
            df_final = pd.merge(
                df_reporte,
                self.df_clientes[['cliente_id', 'nombre']],
                on='cliente_id',
                how='left'
            )
            
            if 'nombre' not in df_final.columns:
                 df_final['nombre'] = df_final['cliente_id']
                 
            return df_final[['nombre', 'Numero de Compras']]
            
        except KeyError as e:
            print(f"Error: Columna faltante {e} en 'clientes.csv' o 'compras.csv'.")
            return pd.DataFrame(columns=['nombre', 'Numero de Compras'])
        except Exception as e:
            print(f"Error inesperado al generar reporte de clientes: {e}")
            return pd.DataFrame(columns=['nombre', 'Numero de Compras'])

    def get_reporte_top_clientes_por_gasto(self, top_n=3):
        if self.df_compras is None or self.df_clientes is None:
            print("Error: Datos de compras no disponibles.")
            return pd.DataFrame(columns=['Cliente', 'Total Gastado'])

        try:
            df_temp = self.df_compras.copy()
            
            if 'cantidad' not in df_temp.columns or 'precio_unitario' not in df_temp.columns:
                 print("Error: Faltan columnas 'cantidad' or 'precio_unitario' en 'compras.csv'")
                 return pd.DataFrame(columns=['Cliente', 'Total Gastado'])

            df_temp['monto'] = df_temp['cantidad'] * df_temp['precio_unitario']

            reporte_series = df_temp.groupby('cliente_id')['monto'].sum()
            
            reporte_top = reporte_series.sort_values(ascending=False).head(top_n)
            
            df_reporte = reporte_top.reset_index()
            df_reporte.columns = ['cliente_id', 'Total Gastado']
            
            df_final = pd.merge(
                df_reporte,
                self.df_clientes[['cliente_id', 'nombre']],
                on='cliente_id',
                how='left'
            )

            if 'nombre' not in df_final.columns:
                 df_final['nombre'] = df_final['cliente_id']
            
            return df_final[['nombre', 'Total Gastado']]

        except KeyError as e:
            print(f"Error: Columna faltante {e} en 'clientes.csv' o 'compras.csv'.")
            return pd.DataFrame(columns=['Cliente', 'Total Gastado'])
        except Exception as e:
            print(f"Error inesperado al generar reporte top clientes: {e}")
            return pd.DataFrame(columns=['Cliente', 'Total Gastado'])
        
    def get_lista_clientes_completa(self):
        if self.df_clientes is None:
            return pd.DataFrame(columns=['cliente_id', 'nombre'])
        try:
            return self.df_clientes[['cliente_id', 'nombre']].sort_values(by='nombre').reset_index(drop=True)
        except KeyError:
            print("Error: Faltan 'cliente_id' o 'nombre' en clientes.csv")
            return pd.DataFrame(columns=['cliente_id', 'nombre'])

    def get_historial_compras(self, cliente_id):
        if self.df_compras is None:
            print("Error: Datos de compras no disponibles.")
            return pd.DataFrame() 

        try:
            historial_df = self.df_compras[self.df_compras['cliente_id'] == cliente_id].copy()
            
            if historial_df.empty:
                return pd.DataFrame()

            historial_df['monto'] = historial_df['cantidad'] * historial_df['precio_unitario']
            historial_df = historial_df.sort_values(by='fecha', ascending=False)
            
            columnas_mostrar = ['fecha', 'producto', 'cantidad', 'precio_unitario', 'monto']
            
            columnas_existentes = [col for col in columnas_mostrar if col in historial_df.columns]
            
            return historial_df[columnas_existentes]

        except KeyError as e:
            print(f"Error: Columna faltante {e} al buscar historial.")
            return pd.DataFrame()
        except Exception as e:
            print(f"Error inesperado al obtener historial: {e}")
            return pd.DataFrame()