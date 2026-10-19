# Tutorial: instalar GitHub Copilot en Visual Studio Code

## 1. Crear o abrir una cuenta de GitHub

Ingresá en [github.com](https://github.com/) e iniciá sesión.

Si todavía no tenés una cuenta, seleccioná **Sign up** y completá el registro.

## 2. Abrir Visual Studio Code

Abrí Visual Studio Code e ingresá en **Extensiones**.

- En Mac: `Shift + Command + X`
- En Windows: `Ctrl + Shift + X`

## 3. Instalar GitHub Copilot

En el buscador de extensiones escribí:

```text
GitHub Copilot
```

Seleccioná la extensión oficial publicada por **GitHub** y presioná **Instalar**.

## 4. Conectar la cuenta de GitHub

Después de instalar la extensión:

1. Hacé clic en el ícono de **Cuentas** de Visual Studio Code.
2. Elegí **Sign in with GitHub to use GitHub Copilot**.
3. Se abrirá una ventana del navegador.
4. Iniciá sesión en GitHub.
5. Aceptá la autorización solicitada.
6. Regresá a Visual Studio Code.

## 5. Abrir Copilot Chat

Hacé clic en el ícono de Copilot ubicado en la parte superior de Visual Studio Code.

También podés abrirlo desde:

```text
View → Chat
```

## 6. Comprobar que funciona

Creá un archivo llamado:

```text
prueba.py
```

Escribí el siguiente comentario:

```python
# Crear una función que calcule el promedio de una lista
```

Presioná `Enter` y esperá unos segundos.

Si Copilot muestra una sugerencia en color gris:

- `Tab`: aceptar la sugerencia.
- `Esc`: rechazar la sugerencia.

También podés escribir en Copilot Chat:

```text
Creá una función sencilla en Python que calcule el promedio de una lista.
```

## Si Copilot no aparece

1. Reiniciá Visual Studio Code.
2. Comprobá que la extensión esté instalada y habilitada.
3. Revisá que tu cuenta de GitHub esté conectada.
4. Abrí la paleta de comandos:
   - Mac: `Command + Shift + P`
   - Windows: `Ctrl + Shift + P`
5. Ejecutá el comando:

```text
Developer: Reload Window
```

## Plan de GitHub Copilot

GitHub ofrece **Copilot Free**, con una cantidad limitada de usos mensuales. Los docentes verificados pueden solicitar acceso gratuito a Copilot Pro.

Más información: [documentación oficial de GitHub Copilot](https://docs.github.com/copilot/managing-copilot/configure-personal-settings/installing-the-github-copilot-extension-in-your-environment).
