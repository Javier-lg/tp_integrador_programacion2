import os

class BaseView:
    def limpiar_pantalla(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def pausa(self):
        print("\nPresione Enter para continuar...")
        input()

    def mostrar_error(self, mensaje):
        print(f"\n[ERROR] {mensaje}")
        self.pausa()