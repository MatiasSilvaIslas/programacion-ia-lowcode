# Clase 4 — Preparación del entorno de Python

## Objetivo

Preparar una carpeta de trabajo con:

- Python 3.12 o superior.
- Visual Studio Code.
- Las extensiones Python y Jupyter.
- Un entorno virtual propio llamado `.venv`.
- Un kernel de Jupyter asociado a esta carpeta.
- Una notebook para comprobar la instalación.

La estructura final será:

```text
clase_4/
├── .venv/
└── 01_preparacion_entorno.ipynb
```

---

# Instalación en Windows

## 1. Instalar Python

1. Ingresar en [python.org/downloads](https://www.python.org/downloads/).
2. Descargar una versión actual de Python.
3. Ejecutar el instalador.
4. Marcar la opción **Add Python to PATH**.
5. Seleccionar **Install Now**.

Abrir PowerShell y comprobar la instalación:

```powershell
python --version
```

Si ese comando no funciona, probar:

```powershell
py --version
```

## 2. Instalar Visual Studio Code

Descargar Visual Studio Code desde [code.visualstudio.com](https://code.visualstudio.com/).

Durante la instalación conviene habilitar:

```text
Add to PATH
Open with Code
```

## 3. Instalar las extensiones

Abrir Visual Studio Code y presionar:

```text
Ctrl + Shift + X
```

Instalar las siguientes extensiones:

- **Python**, publicada por Microsoft.
- **Jupyter**, publicada por Microsoft.
- **GitHub Copilot**, publicada por GitHub.

## 4. Crear la carpeta de trabajo

Desde PowerShell:

```powershell
mkdir clase_4
cd clase_4
code .
```

El comando `code .` abre en Visual Studio Code la carpeta en la que estamos ubicados.

## 5. Abrir la terminal de Visual Studio Code

Dentro de Visual Studio Code seleccionar:

```text
Terminal → New Terminal
```

Comprobar que la terminal se encuentre dentro de la carpeta `clase_4`.

## 6. Crear un entorno virtual

Ejecutar:

```powershell
py -3.13 -m venv .venv
```

Si esa versión no está disponible, utilizar:

```powershell
python -m venv .venv
```

### ¿Por qué necesitamos un entorno virtual?

Un entorno virtual es una instalación de Python aislada para una carpeta o proyecto.

Nos permite:

- Instalar paquetes sin modificar el Python general de la computadora.
- Evitar conflictos entre proyectos que utilizan versiones diferentes de una biblioteca.
- Saber exactamente qué intérprete y qué paquetes utiliza el programa.
- Crear un kernel de Jupyter específico para esta carpeta.
- Eliminar y volver a crear el entorno si algo deja de funcionar.

La carpeta `.venv` contiene el intérprete y los paquetes propios del proyecto. Cada carpeta de trabajo puede tener su propio `.venv`.

> La carpeta `.venv` no contiene nuestro código y no debe subirse al repositorio de GitHub.

## 7. Activar el entorno virtual

```powershell
.venv\Scripts\activate
```

Si se activó correctamente, la terminal comenzará con:

```text
(.venv)
```

Comprobar la versión:

```powershell
python --version
```

## 8. Instalar el kernel de Jupyter

Con el entorno activado:

```powershell
python -m pip install --upgrade pip
python -m pip install ipykernel
```

## 9. Registrar un kernel para esta carpeta

```powershell
python -m ipykernel install --user --name programacion-ia-clase4 --display-name "Python — Clase 4"
```

- `programacion-ia-clase4` es el nombre interno del kernel.
- `Python — Clase 4` es el nombre que aparecerá en Visual Studio Code.

---

# Instalación en macOS

## 1. Instalar Python

1. Ingresar en [python.org/downloads](https://www.python.org/downloads/).
2. Descargar una versión actual de Python para macOS.
3. Ejecutar el instalador.

Abrir Terminal y comprobar la instalación:

```bash
python3 --version
```

## 2. Instalar Visual Studio Code

Descargarlo desde [code.visualstudio.com](https://code.visualstudio.com/) y mover la aplicación a la carpeta **Aplicaciones**.

## 3. Habilitar el comando `code`

En Visual Studio Code:

1. Presionar `Command + Shift + P`.
2. Buscar el siguiente comando:

```text
Shell Command: Install 'code' command in PATH
```

3. Ejecutarlo.

## 4. Instalar las extensiones

Abrir el panel de extensiones con:

```text
Shift + Command + X
```

Instalar:

- **Python**, publicada por Microsoft.
- **Jupyter**, publicada por Microsoft.
- **GitHub Copilot**, publicada por GitHub.

## 5. Crear la carpeta de trabajo

Desde Terminal:

```bash
mkdir clase_4
cd clase_4
code .
```

## 6. Abrir la terminal de Visual Studio Code

Dentro de Visual Studio Code seleccionar:

```text
Terminal → New Terminal
```

## 7. Crear un entorno virtual

Ejecutar:

```bash
python3.13 -m venv .venv
```

Si ese comando no funciona, utilizar:

```bash
python3 -m venv .venv
```

### ¿Por qué necesitamos un entorno virtual?

Un entorno virtual es una instalación de Python aislada para una carpeta o proyecto.

Nos permite:

- Instalar paquetes sin modificar el Python general de la computadora.
- Evitar conflictos entre proyectos que necesitan paquetes o versiones diferentes.
- Mantener separadas las dependencias de cada trabajo.
- Crear un kernel de Jupyter asociado a esta carpeta.
- Borrar y reconstruir el entorno sin perder nuestros programas.

La carpeta `.venv` pertenece únicamente al proyecto `clase_4`. Al activarla, los comandos `python` y `pip` utilizan este entorno y no otro Python instalado en la computadora.

> La carpeta `.venv` no debe subirse al repositorio de GitHub.

## 8. Activar el entorno virtual

```bash
source .venv/bin/activate
```

Si se activó correctamente, la terminal comenzará con:

```text
(.venv)
```

Comprobar la versión:

```bash
python --version
```

## 9. Instalar el kernel de Jupyter

Con el entorno activado:

```bash
python -m pip install --upgrade pip
python -m pip install ipykernel
```

## 10. Registrar un kernel para esta carpeta

```bash
python -m ipykernel install --user \
  --name programacion-ia-clase4 \
  --display-name "Python — Clase 4"
```

---

# Crear la notebook

## 1. Crear una notebook nueva

Abrir la paleta de comandos:

- macOS: `Command + Shift + P`
- Windows: `Ctrl + Shift + P`

Buscar y ejecutar:

```text
Jupyter: Create New Blank Notebook
```

## 2. Guardar la notebook

Guardarla dentro de `clase_4` con el nombre:

```text
01_preparacion_entorno.ipynb
```

## 3. Seleccionar el kernel

1. Presionar **Seleccionar kernel** en la esquina superior derecha.
2. Elegir **Python — Clase 4**.

Si no aparece, abrir la paleta de comandos y ejecutar:

```text
Developer: Reload Window
```

Luego volver a seleccionar el kernel.

---

# Comprobar que el kernel es correcto

En la primera celda escribir:

```python
import sys

print("Versión:", sys.version)
print("Intérprete:", sys.executable)
```

La ruta mostrada debe contener:

```text
clase_4/.venv
```

En macOS será similar a:

```text
/.../clase_4/.venv/bin/python
```

En Windows será similar a:

```text
...\clase_4\.venv\Scripts\python.exe
```

Esto confirma que la notebook utiliza el Python de esta carpeta y no otro kernel instalado en la computadora.

---

# Prueba final

Crear otra celda y ejecutar:

```python
productos: list[str] = ["Lámpara", "Silla", "Mesa"]

for producto in productos:
    print(producto)

print("El entorno de la Clase 4 funciona correctamente.")
```

Para salir del entorno virtual desde la terminal:

```bash
deactivate
```
