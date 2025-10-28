import os
import matplotlib.pyplot as plt
import pandas as pd
from views.base_view import BaseView

class VentasView(BaseView):
    def __init__(self, items_por_pagina=5):
        self.items_por_pagina= items_por_pagina

    def mostrar_menu_productos_paginado(self, productos):
        pagina_actual = 0
        total_paginas = max(1, (len(productos) -1) // self.items_por_pagina + 1)

        while True:
            self.limpiar_pantalla()
            print("--- Seleccione un producto para analizar ---")

            inicio = pagina_actual * self.items_por_pagina
            fin = inicio + self.items_por_pagina
            productos_pagina = productos[inicio:fin]

            for i, producto in enumerate(productos_pagina):
                print(f" {inicio + i + 1}. {producto}")

            print("\n" + "-"*30)
            print(f"Página {pagina_actual + 1} de {total_paginas}")
            print("Opciones:")
            print("  [reporte_categorias] Reporte de ventas por categoria")
            if fin < len(productos):
                print("  [s] Siguiente pagina (Ver mas)")
            if pagina_actual > 0:
                print("  [a] Pagina anterior")
            print("  [v] Salir del programa")
            print("-" * 30)

            opcion = input("Ingrese el NUMERO del producto o una opción (reporte_categorias/s/a/v): ").strip().lower()
            
            if opcion.isdigit():
                opcion_num = int(opcion)
                if 1 <= opcion_num <= len(productos):
                    if (inicio + 1 <= opcion_num <= fin):
                        return productos[opcion_num - 1] # Retorna el nombre del producto
                    else:
                        print(f"\n'{opcion_num}' no esta en esta página. Buscando...")
                        
                        pagina_actual = (opcion_num - 1) // self.items_por_pagina
                else:
                    print(f"\nError: '{opcion_num}' no es un numero de producto válido.")
                    self.pausa()
            elif opcion == 's' and fin < len(productos):
                pagina_actual += 1
            elif opcion == 'a' and pagina_actual > 0:
                pagina_actual -= 1
            elif opcion == 'v':
                return None
            elif opcion == 'reporte_categorias':
                return 'reporte'
            else:
                print(f"\nError: Opcion '{opcion}' no reconocida.")
                self.pausa()


    def mostrar_titulo_reporte(self, producto):
        """
        Muestra un encabezado claro para el reporte.
        """
        print("=================================================")
        print(f"  Análisis del Producto: {producto.upper()}")
        print("=================================================")

    def mostrar_reporte_producto(self, resumen, datos_np):
        if resumen['total'] == 0:
            print("No se registraron ventas para este producto.")
            return

        print("\n--- Resumen Estadístico ---")
        print(f"Total Vendido:    ${resumen['total']:,.2f}")
        print(f"Promedio Mensual: ${resumen['promedio']:,.2f}")
        print(f"Mes con Mayor Venta: {resumen['mes_max']} (Max)")
        print(f"Mes con Menor Venta: {resumen['mes_min']} (Min)")
        
        print("\nDesglose por Sucursal:")
        if not resumen['por_sucursal']:
            print("  No hay datos por sucursal.")
        else:
            sucursales_ord = sorted(resumen['por_sucursal'].items(), key=lambda item: item[1], reverse=True)
            for s, v in sucursales_ord:
                print(f"  - {s:<10} ${v:,.2f}")

        print("\n--- Analisis Detallado ---")
        print(f"Meses analizados:     {datos_np['indices']}")
        print(f"Valores de venta:     {datos_np['valores'].round(2)}")
        print(f"¿Supera promedio?:    {datos_np['mask']}")
        print(f"Valores ordenados (min a max):")
        print(f"  {datos_np['ordenados'].round(2)}")

    def graficar_linea(self, mensual_series, producto):
        if mensual_series.empty:
            print("\nNo hay datos mensuales para graficar la evolución.")
            return

        x = [str(p) for p in mensual_series.index]
        y = mensual_series.values
        
        plt.figure(figsize=(10, 6))
        plt.plot(x, y, marker='o', linestyle='-', color='b') # Estilo
        
        plt.title(f'Evolución de Ventas Mensuales: {producto}', fontsize=16)
        plt.xlabel('Mes (Año-Mes)', fontsize=12)
        plt.ylabel('Monto Vendido ($)', fontsize=12)
        
        plt.xticks(rotation=45, ha='right')
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        
        plt.show()

    def graficar_torta(self, cat_series, titulo):
        
        if cat_series.empty:
            print("\nNo hay datos de categorias para graficar la torta.")
            return
            
        valores = cat_series.values
        etiquetas = cat_series.index
        
        plt.figure(figsize=(7, 7)) # Tamaño
        plt.pie(valores, labels=etiquetas, autopct='%1.1f%%',
                startangle=90, pctdistance=0.85)
        
        centre_circle = plt.Circle((0,0),0.70,fc='white')
        fig = plt.gcf()
        fig.gca().add_artist(centre_circle)
        
        plt.title(titulo, fontsize=16)
        plt.axis('equal')
        plt.tight_layout()
        
        plt.show()
