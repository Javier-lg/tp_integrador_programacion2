from views.base_view import BaseView

class MenuView(BaseView):
    def __init__(self):
        super().__init__()

    def mostrar_bienvenida(self):
        self.limpiar_pantalla()
        print("=================================================")
        print("   Sistema de Análisis de Ventas - Examen Final")
        print("   Autor: Salinas Lavayen Roberto Javier")
        print("   Materia: Programación II - UCASAL")
        print("=================================================\n")
        print("Este proyecto implementa un análisis de datos de ventas")
        print("utilizando Pandas, NumPy y Matplotlib, estructurado")
        print("bajo una arquitectura Modelo-Vista-Controlador (MVC).")
        self.pausa()

    def mostrar_despedida(self):
        self.limpiar_pantalla()
        print("=========================================")
        print(" Gracias por utilizar el sistema.")
        print(" Valar Morghulis")
        print("=========================================")

    def mostrar_menu_principal(self):
        while True:
            self.limpiar_pantalla()
            print("--- Menu Principal ---")
            print("Seleccione un modulo para operar:")
            print("")
            print("  [1] Modulo de Ventas")
            print("  [2] Modulo de Clientes")
            print("")
            print("  [0] Salir del Programa")
            print("-" * 30)
            
            opcion = input("Ingrese su opción: ").strip()

            if opcion in ['1', '2', '0']:
                return opcion
            else:
                self.mostrar_error("Opción no válida. Intente nuevamente.")