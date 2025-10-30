import pandas as pd
from views.base_view import BaseView

class ClientesView(BaseView):

    def __init__(self, items_por_pagina=10):
        super().__init__()
        self.items_por_pagina = items_por_pagina

    def mostrar_menu_clientes(self):
        while True:
            self.limpiar_pantalla()
            print("--- Módulo de Clientes ---")
            print("Seleccione una opción:")
            print("")
            print("  [1] Ver listado de todos los clientes")
            print("  [2] Reporte: Top 3 clientes más activos")
            print("  [3] Reporte: Top 3 clientes por gasto total")
            print("  [4] Ver historial de compras de un cliente")
            print("")
            print("  [0] Volver al Menú Principal")
            print("-" * 30)
            
            opcion = input("Ingrese su opción: ").strip()

            if opcion in ['1', '2', '3', '4', '0']:
                return opcion
            else:
                self.mostrar_error("Opción no válida. Intente nuevamente.")

    def mostrar_listado_clientes(self, clientes):
        self.limpiar_pantalla()
        print("--- Listado de Clientes Registrados ---")
        if not clientes:
            print("No hay clientes para mostrar.")
        else:
            for i, cliente in enumerate(clientes):
                print(f"  {i+1}. {cliente}")
        
        self.pausa()

    def mostrar_reporte_tabular(self, df_reporte, titulo):
        self.limpiar_pantalla()
        print(f"--- {titulo} ---")
        
        if df_reporte is None or df_reporte.empty:
            print("No hay datos para mostrar en este reporte.")
        else:
            # Asegurarse que los nombres de columna coincidan con el modelo
            if 'Total Gastado' in df_reporte.columns:
                 print(df_reporte.to_string(index=False, formatters={'Total Gastado': '${:,.2f}'.format}))
            else:
                 print(df_reporte.to_string(index=False))
        
        self.pausa()

    def seleccionar_cliente(self, clientes_df):
        if clientes_df.empty:
            self.mostrar_error("No hay clientes en la base de datos.")
            return None

        clientes_lista = list(clientes_df.itertuples(index=False))
        pagina_actual = 0
        total_paginas = max(1, (len(clientes_lista) - 1) // self.items_por_pagina + 1)

        while True:
            self.limpiar_pantalla()
            print("--- Seleccione un Cliente para ver su Historial ---")

            inicio = pagina_actual * self.items_por_pagina
            fin = inicio + self.items_por_pagina
            clientes_pagina = clientes_lista[inicio:fin]

            for i, cliente_tupla in enumerate(clientes_pagina):
                print(f"  {inicio + i + 1}. {cliente_tupla[1]} (ID: {cliente_tupla[0]})") 

            print("\n" + "-"*30)
            print(f"Página {pagina_actual + 1} de {total_paginas}")
            print("Opciones:")
            if fin < len(clientes_lista):
                print("  [s] Siguiente pagina")
            if pagina_actual > 0:
                print("  [a] Pagina anterior")
            print("  [v] Volver al menú de clientes")
            print("-" * 30)

            opcion = input("Ingrese el NÚMERO del cliente o una opción (s/a/v): ").strip().lower()
            
            if opcion.isdigit():
                opcion_num = int(opcion)
                if 1 <= opcion_num <= len(clientes_lista):
                    cliente_seleccionado = clientes_lista[opcion_num - 1]
                    return cliente_seleccionado[0]
                else:
                    self.mostrar_error(f"'{opcion_num}' no es un número de cliente válido.")
            elif opcion == 's' and fin < len(clientes_lista):
                pagina_actual += 1
            elif opcion == 'a' and pagina_actual > 0:
                pagina_actual -= 1
            elif opcion == 'v':
                return None
            else:
                self.mostrar_error(f"Opción '{opcion}' no reconocida.")

    def mostrar_historial_compras(self, historial_df, nombre_cliente):
        self.limpiar_pantalla()
        print(f"--- Historial de Compras: {nombre_cliente} ---")
        
        if historial_df.empty:
            print("Este cliente no tiene compras registradas.")
        else:
            historial_df['fecha'] = pd.to_datetime(historial_df['fecha']).dt.strftime('%Y-%m-%d')
            
            formatters = {
                'precio_unitario': '${:,.2f}'.format,
                'monto': '${:,.2f}'.format
            }
            
            print(historial_df.to_string(index=False, formatters=formatters))
            
            total = historial_df['monto'].sum()
            print("-" * (len(historial_df.to_string(index=False).split('\n')[0]))) # Separador dinámico
            print(f"GASTO TOTAL HISTÓRICO: ${total:,.2f}")
        
        self.pausa()