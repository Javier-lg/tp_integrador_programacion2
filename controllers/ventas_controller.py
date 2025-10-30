from models.ventas_model import VentasModel
from views.ventas_view import VentasView

class VentasController:
    def __init__(self):
        self.model = VentasModel()
        self.view = VentasView()

    def run(self):
        if self.model.get_dataframe() is None:
            self.view.mostrar_error("Fallo al cargar datos")

            return 
        

        while True:
            productos = self.model.get_productos_unicos()

            if not productos:
                self.view.mostrar_error("No se encontrar productos.")
                break

            eleccion = self.view.mostrar_menu_productos_paginado(productos)

            if eleccion == 'reporte_categorias':
                self.analizar_categorias()

            if eleccion == 'reporte_sucursales':
                self.analizar_sucursales()

            elif eleccion is None:
                break
            
            else:
                self.view.limpiar_pantalla()
                self.analizar_producto(eleccion)

                self.view.pausa()

    def analizar_producto(self, producto):
        self.view.mostrar_titulo_reporte(producto)

        resumen = self.model.resumen_producto(producto)
        if resumen is None:
            self.view.mostrar_error(f"No se encontrar datos para '{producto}'")
            return
        
        datos_np = self.model.mascaras_numpy(resumen['mensual'])

        self.view.mostrar_reporte_producto(resumen, datos_np)

        self.view.graficar_linea(resumen['mensual'], producto)

    def analizar_categorias(self):
        datos_torta_cat = self.model.get_datos_torta_categorias()
        self.view.graficar_torta(datos_torta_cat, "Participacion por categoria")

    def analizar_sucursales(self):
        self.view.limpiar_pantalla()
        try:
            reporte_datos = self.model.get_reporte_sucursales()

            self.view.mostrar_reporte_sucursales(reporte_datos)

            self.view.graficar_barras_sucursales(reporte_datos)
        except Exception as e:
            self.view.mostrar_error(f"Error al generar reporte de sucursales: {e}")