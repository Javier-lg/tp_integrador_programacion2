import pandas as pd
import numpy as np

from utils.helpers import normalizar_texto
from utils.db_conn import CSVDatabase

class VentasModel:
    def __init__(self, db_path='data/ventas.csv'):
        self.db = CSVDatabase(path=db_path)
        self.df = None

        if self.db.verificar_csv():
            self.df = self.db.leer_csv()
        else:
            pass

    def get_dataframe(self):
        return self.df
    
    def get_productos_unicos(self):
        if self.df is None:
            return []
        
        productos = sorted(list(self.df['producto'].unique()))
        return productos
    
    def resumen_producto(self, producto):
        if self.df is None:
            return None
        
        dfp = self.df[self.df['producto'].str.lower().str.strip() == producto.lower().strip()].copy()
        
        if dfp.empty:
            return None
        
        dfp['monto'] = dfp['cantidad'] * dfp['precio_unitario']
        dfp['año_mes'] = dfp['fecha'].dt.to_period('M')

        mensual = dfp.groupby('año_mes')['monto'].sum().sort_index()

        if mensual.empty:
            return {'mensual': mensual, 'total': 0, 'promedio': 0,
                    'mes_max': 'N/A', 'mes_min': 'N/A', 'por_sucursal': {}}
        
        total = mensual.sum()
        promedio = mensual.mean()
        mes_max = mensual.idxmax().strftime('%Y-%m')
        mes_min = mensual.idxmin().strftime('%Y-%m')
        por_sucursal = dfp.groupby('sucursal')['monto'].sum().to_dict()

        return {'mensual': mensual, 'total': float(total), 'promedio': float(promedio),
                'mes_max': mes_max, 'mes_min':mes_min, 'por_sucursal': por_sucursal}
    
    def mascaras_numpy(self, mensual):
        if mensual.empty:
            return {'indices': np.array([]), 'valores': np.array([]), 
                    'mask': np.array([]), 'ordenados': np.array([])}
        
        valores = mensual.values.astype(float)
        indices = np.array([str(x) for x in mensual.index.astype(str)])
        mask_mayor_prom = valores > valores.mean()
        ordenados = np.sort(valores)

        return {'indices':indices,'valores':valores,'mask':mask_mayor_prom,'ordenados':ordenados}
    
    def get_datos_torta_categorias(self):
        if self.df is None:
            return pd.Series(dtype=float)
            
        df2 = self.df.copy()
        df2['monto'] = df2['cantidad'] * df2['precio_unitario']
        cat = df2.groupby('categoria')['monto'].sum()
        return cat