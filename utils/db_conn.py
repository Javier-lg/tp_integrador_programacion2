import os
import random
from datetime import datetime, timedelta
import pandas as pd

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
