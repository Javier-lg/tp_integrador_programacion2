from controllers.ventas_controller import VentasController

from views.menu_view import MenuView
from views.base_view import BaseView

class MainController:
    def __init__(self):
        self.menu_view = MenuView()

    def run(self):

        while True:
            opcion = self.menu_view.mostrar_menu_principal()

            if opcion == '1':
                try:
                    ventas_app = VentasController()
                    ventas_app.run()

                except Exception as e:
                    self.menu_view.mostrar_error(f"Ocurrio un error en el modulo de ventas: {e}")
            
            elif opcion == '2':
                self.menu_view.mostrar_error("Modulo noimplementado todavia")

            elif opcion == '0':
                break