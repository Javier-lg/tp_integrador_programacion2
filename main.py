from controllers.main_controller import MainController

def main():
    print("iniciando app...")
    try:
        app = MainController()

        app.run()

    except ImportError as e:
        print(f"Error fatal de importacion: {e}")

    except Exception as e:
        print(f"Error inesperado:{e}")
    
    finally:
        print("app finalizada")

if __name__ == '__main__':
    main()