# Proyecto de Ventas

Este proyecto implementa una arquitectura **MVC (Modelo-Vista-Controlador)** en Python para la gestión de ventas.  
Incluye módulos para modelos, vistas y controladores, con un punto de entrada principal (`main.py`).

---

## Requisitos Previos

Asegúrate de tener instalado:

- [Python 3.10+](https://www.python.org/downloads/)
- `pip` (gestor de paquetes de Python)

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

## Autor

Desarrollado por **javier-lg**