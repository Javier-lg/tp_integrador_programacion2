from models.clientes_model import ClientesModel
from views.clientes_view import ClientesView

class ClientesController:
    
    def __init__(self):
        self.model = ClientesModel()
        self.view = ClientesView()

    def run(self):
        if self.model.df_clientes is None or self.model.df_compras is None:
            self.view.mostrar_error("Fallo al cargar datos de clientes o compras. Volviendo al menú.")
            return

        while True:
            opcion = self.view.mostrar_menu_clientes()

            if opcion == '1':
                self.listar_todos_clientes()
            
            elif opcion == '2':
                self.mostrar_clientes_activos()
            
            elif opcion == '3':
                self.mostrar_clientes_top_gasto()

            elif opcion == '4':
                self.ver_historial_cliente()

            elif opcion == '0':
                break

    def listar_todos_clientes(self):
        lista_clientes = self.model.get_clientes_unicos()
        self.view.mostrar_listado_clientes(lista_clientes)

    def mostrar_clientes_activos(self):
        reporte_df = self.model.get_reporte_clientes_activos(top_n=3)
        self.view.mostrar_reporte_tabular(reporte_df, "Top 3 Clientes Más Activos (por N° de Compras)")
    
    def mostrar_clientes_top_gasto(self):
        reporte_df = self.model.get_reporte_top_clientes_por_gasto(top_n=3)
        self.view.mostrar_reporte_tabular(reporte_df, "Top 3 Clientes (por Gasto Total)")

    def ver_historial_cliente(self):
        clientes_df = self.model.get_lista_clientes_completa()
        if clientes_df.empty:
            self.view.mostrar_error("No se pudo obtener la lista de clientes.")
            return

        cliente_id_seleccionado = self.view.seleccionar_cliente(clientes_df)

        if cliente_id_seleccionado:
            historial_df = self.model.get_historial_compras(cliente_id_seleccionado)
            
            try:
                nombre_cliente = clientes_df.loc[clientes_df['cliente_id'] == cliente_id_seleccionado, 'nombre'].iloc[0]
            except:
                nombre_cliente = f"ID {cliente_id_seleccionado}"

            self.view.mostrar_historial_compras(historial_df, nombre_cliente)