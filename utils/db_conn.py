import os
import random
from datetime import datetime, timedelta
import pandas as pd

class CSVProductosDB:
    def __init__(self, path='data/productos.csv'):
        """ Almacena la ruta al archivo de productos. """
        if not os.path.dirname(path):
             self.path = os.path.join('data', path)
        else:
             self.path = path


    def verificar_csv(self):
        if not os.path.exists(self.path):
            print(f"Error Critico: No se encuentra el archivo de productos en '{self.path}'.")
            print("Asegúrese de que el archivo 'productos.csv' exista en la carpeta 'data'.")
            return False

        if os.path.getsize(self.path) == 0:
            print(f"Error Critico: El archivo '{self.path}' está vacio.")
            return False

        return True

    def leer_csv(self):
        try:
            return pd.read_csv(self.path)

        except FileNotFoundError:
            print(f"Error: No se encontró el archivo en '{self.path}'")
            return None
        except pd.errors.EmptyDataError:
            print(f"Error: El archivo '{self.path}' esta vacio")
            return None
        except Exception as e:
            print(f"Error inesperado al leer el archivo {self.path}: {e}")
            return None

class CSVDatabase:

    def __init__(self, path='data/ventas.csv'):

        self.path = path

    def verificar_csv(self):
        if not os.path.exists(self.path):
            print("Error Critico: No se encuentra el archivo csv.")
            print("Ubiquelo en /data")
            return False
        
        if os.path.getsize(self.path) == 0:
            print(f"Error Critico: El archivo '{self.path}' esta vacio.")
            return False
        
        return True
    
    def leer_csv(self):
        try:
            return pd.read_csv(self.path, parse_dates=['fecha'])
        
        except FileNotFoundError:
            print(f"Error:No se encontro el archivo en '{self.path}'")
            return None
        except pd.errors.EmptyDataError:
            print(f"Error: El archivo '{self.path}' esta vacio")
            return None
        except Exception as e:
            print(f"Error inesperado al leer el archivo {self.path}: {e}")
            return None
