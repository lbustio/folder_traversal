# Proyecto de Generación de Esquema de Directorio

Este proyecto utiliza un script en Python para listar y generar un esquema de un directorio de forma recursiva, mostrando la estructura de carpetas y archivos dentro de un directorio base. El resultado se guarda en un archivo de texto.

## Estructura del Proyecto

El proyecto consta de los siguientes elementos principales:

- `listar_directorio(directorio, nivel=0)`: Función que lista recursivamente el contenido de un directorio, generando una estructura con la indentación correspondiente a cada nivel de subcarpetas.
- `ruta_base`: Ruta base donde se encuentra el directorio del cual se generará el esquema.
- El resultado final se guarda en un archivo de texto llamado `esquema_directorio.txt`.

## Uso

### Requisitos

- Python 3.x
- Permisos de lectura en el directorio del cual se desea generar el esquema.

### Instrucciones

1. Clona este repositorio o descarga los archivos.
2. Asegúrate de tener instalada la versión de Python 3.x.
3. Modifica la variable `ruta_base` en el script con la ruta del directorio que desees listar.
4. Ejecuta el script usando Python:

    ```bash
    python script.py
    ```

5. El esquema del directorio se generará en un archivo de texto llamado `esquema_directorio.txt` en la misma carpeta del script.

### Ejemplo de Salida

Si el directorio base tiene la siguiente estructura:

📁 ml-project-name  
├── .gitignore  
├── 📁 data  
├── 📁 model  
└── 📄 main.py

El archivo `esquema_directorio.txt` tendrá el siguiente contenido:

ml-project-name

- data
- models
- main.py

### Modificaciones

- Para cambiar el nivel de indentación o ajustar el formato del esquema, puedes modificar el parámetro `nivel` en la función `listar_directorio`.

## Contribuciones

Si deseas contribuir, puedes hacerlo creando un _fork_ del proyecto, haciendo tus cambios y luego creando un _pull request_.

## Licencia

Este proyecto está bajo la licencia MIT.
