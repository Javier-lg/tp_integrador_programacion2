import os
import pandas as pd

class CSVBase:
    def __init__(self, path, parse_dates=None):
        if not os.path.dirname(path):
             self.path = os.path.join('data', path)
        else:
             self.path = path
        
        self.parse_dates = parse_dates

    def verificar_csv(self):
        if not os.path.exists(self.path):
            print(f"Error Crítico: No se encuentra el archivo en '{self.path}'.")
            return False
        
        if os.path.getsize(self.path) == 0:
            print(f"Error Crítico: El archivo '{self.path}' está vacío.")
            return False
        
        return True
    
    def leer_csv(self):
        try:
            return pd.read_csv(self.path, parse_dates=self.parse_dates)
        
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo en '{self.path}'")
            return None
        except pd.errors.EmptyDataError:
            print(f"Error: El archivo '{self.path}' está vacío")
            return None
        except Exception as e:
            print(f"Error inesperado al leer el archivo {self.path}: {e}")
            return None

class CSVDatabase(CSVBase):
    def __init__(self, path='data/ventas.csv'):
        super().__init__(path=path, parse_dates=['fecha'])

class CSVProductosDB(CSVBase):
    def __init__(self, path='data/productos.csv'):
        super().__init__(path=path, parse_dates=None)

class CSVComprasDB(CSVBase):
    def __init__(self, path='data/compras.csv'):
        super().__init__(path=path, parse_dates=['fecha'])

class CSVClientesDB(CSVBase):
    def __init__(self, path='data/clientes.csv'):
        super().__init__(path=path, parse_dates=None)