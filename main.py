from controllers.ventas_controller import VentasController

def main():
    print("iniciando app...")
    try:
        app = VentasController()

        app.run()

    except ImportError as e:
        print(f"Error fatal de importacion: {e}")

    except Exception as e:
        print(f"Error inesperado:{e}")
    
    finally:
        print("app finalizada")

if __name__ == '__main__':
    main()