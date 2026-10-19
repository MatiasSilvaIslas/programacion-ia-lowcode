# API de inscripciones

API educativa desarrollada con FastAPI para practicar la recepción y validación de inscripciones a cursos. Recibe nombre, edad, curso y correo electrónico; comprueba que los datos tengan el formato esperado y determina si la inscripción se acepta directamente o requiere autorización de una persona adulta.

## Requisitos

- Python 3.10 o posterior (recomendado).
- PowerShell en Windows.

## Crear el entorno e instalar dependencias

Desde la carpeta `Clase 6/api-inscripciones`, crea y activa un entorno virtual:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Si PowerShell bloquea la activación del entorno, ejecuta `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` en esa terminal y vuelve a activar el entorno.

Instala las dependencias del proyecto:

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

El archivo `requirements.txt` incluye `email-validator`, necesario para validar el campo de correo electrónico `EmailStr` de Pydantic.

## Ejecutar la API con Uvicorn

Con el entorno virtual activo y situado en `Clase 6/api-inscripciones`, inicia el servidor de desarrollo:

```powershell
python -m uvicorn app.main:app --reload
```

La API queda disponible en `http://127.0.0.1:8000`. Detén el servidor con `Ctrl+C`.

## Documentación interactiva (Swagger)

Abre [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) para explorar y probar los endpoints desde Swagger UI. La documentación alternativa de ReDoc está en [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc).

## Endpoints

| Método | Ruta | Descripción |
| --- | --- | --- |
| `GET` | `/` | Mensaje de bienvenida y confirmación de que la API está en funcionamiento. |
| `GET` | `/status` | Estado del servicio. |
| `POST` | `/validar-inscripcion` | Valida una inscripción y devuelve el resultado según la edad. |

El endpoint `POST /validar-inscripcion` espera un objeto JSON con `nombre` (no puede estar vacío), `edad` (entero entre 0 y 120), `curso` y `email` (dirección de correo válida). Para personas menores de 18 años, la respuesta indica que se requiere autorización de una persona adulta.