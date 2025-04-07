# Sistema de Gestión de Contactos

Este proyecto implementa un sistema de gestión de contactos en Python. El sistema permite realizar operaciones básicas como agregar, mostrar, buscar y eliminar contactos, además de manejar un archivo de texto para almacenar y cargar los datos de los contactos.

## Características principales
1. **Agregar contacto**: Permite al usuario añadir un contacto con los campos:
   - Nombre
   - Teléfono
   - Correo electrónico
   - Valida que el correo electrónico tenga un formato correcto.
2. **Mostrar contactos**: Muestra todos los contactos almacenados.
3. **Buscar contacto**: Permite buscar un contacto por su nombre.
4. **Eliminar contacto**: Elimina un contacto de la lista basado en su nombre.
5. **Persistencia de datos**: Usa un archivo de texto (`contactos.txt`) para guardar los contactos, asegurando que los datos se mantengan entre ejecuciones.
6. **Gestión de errores**: Maneja situaciones como:
   - Contactos con datos mal formateados en el archivo.
   - Intentos de buscar o eliminar contactos inexistentes.
   - Errores al leer o escribir en el archivo.

## Requisitos
- **Python 3.8 o superior**
- El archivo `contactos.txt` debe estar ubicado en la misma carpeta que los archivos del proyecto o en la ruta especificada en el código.

## Cómo ejecutar el sistema
1. Clona el repositorio:
   git clone https://github.com/AndresFelipeR/GestionContactos-Phyton.git
2.Navegar al directorio del proyecto
  cd GestionContactos-Phyton
3.Ejecutar el archivo principal
  python Menu.py

## Archivos del proyecto
1. Menu.py: Contiene la interfaz principal para interactuar con el sistema.
2. GestionContacto.py: Implementa la lógica del sistema de gestión de contactos.
3. Contacto.py: Define la estructura de un contacto.
4. contactos.txt: Archivo donde se guardan los contactos registrados.

## Poe que se realiza
 Este Proyecto se realiza como practica en el Curso de Formación Avanzada en Backend: Python, Flask y Django
en el modulo 2
