## Autor

Desarrollado por **javier-lg** - **SALINAS LAVAYEN ROBERTO JAVIER**

# Proyecto de Ventas

Este proyecto implementa una arquitectura **MVC (Modelo-Vista-Controlador)** en Python para la gestión y análisis de ventas.  
Incluye módulos para modelos, vistas y controladores, con un punto de entrada principal (`main.py`).

---

## Consigna del Trabajo Integrador

Se requiere crear un programa capaz de analizar un archivo de datos de ventas.

Si el archivo no existe, el sistema debe generarlo automáticamente con datos ficticios que incluyan fecha, sucursal, producto, categoría, cantidad y precio.

El sistema debe permitir al usuario ingresar el nombre de un producto para analizar.  
Para el producto seleccionado, el programa debe calcular y mostrar un resumen estadístico que incluya el total vendido, el promedio mensual, el mes de mayor y menor venta, y las ventas por sucursal.  
Además, debe mostrar un análisis detallado de la serie mensual, indicando los valores de cada mes, cuáles superan el promedio y el listado ordenado de valores.

También se deben generar visualizaciones que representen la evolución de las ventas mensuales y la participación de las categorías en el total de ventas.

Por último, el sistema debe permitir visualizar información de los clientes, incluyendo la lista completa, los clientes con mayor gasto, los más activos y el historial de compras de cada uno.

---

## Requisitos Previos

Asegúrate de tener instalado:

- Python 3.10 o superior
- pip (gestor de paquetes de Python)

---

## Configuración del Entorno Virtual

### En Windows

Abre una terminal en la raíz del proyecto y ejecuta:

```bash
python -m venv .venv
```

Activa el entorno virtual:

```bash
.venv\Scripts\activate
```

Instala las dependencias:

```bash
pip install -r requirements.txt
```

### En Linux / macOS

Crea el entorno virtual:

```bash
python3 -m venv .venv
```

Actívalo:

```bash
source .venv/bin/activate
```

Instala las dependencias:

```bash
pip install -r requirements.txt
```

---

## Ejecución del Proyecto

Con el entorno virtual activo, ejecuta:

```bash
python main.py
```

(o en Linux/macOS)

```bash
python3 main.py
```

---

## Desactivar el Entorno

Cuando termines de trabajar:

```bash
deactivate
```

---

## Notas

- El archivo `requirements.txt` contiene las dependencias necesarias para correr el proyecto.
- Si agregas nuevas dependencias, recuerda actualizarlo con:

  ```bash
  pip freeze > requirements.txt
  ```

- La carpeta `.venv` **no debe subirse** al repositorio (ya está ignorada por `.gitignore`).

---


