import os
import re
from Contacto import Contacto

class GestionContacto:
    
    def __init__(self,archivo="contactos.txt"):
        self.contactos = []
        self.archivo = archivo
        self.cargar_contactos()
# Funcion para cargar los contactos desde el archivo
    def cargar_contactos(self):
        if os.path.exists(self.archivo): # verifica si el archivo existe
            try:
                with open(self.archivo, "r", encoding="utf-8") as file: # abre el archivo en modo lectura
                    for linea in file: # lee cada linea del archivo
                        try:
                            nombre, telefono , correo = linea.strip().split(",") # separa los campos por comas
                            if nombre and telefono and correo: # verifica que los campos no esten vacios
                                self.contactos.append(Contacto(nombre,telefono,correo)) # crea un nuevo objeto Contacto con los datos leidos del archivo y lo agrega a la lista de contactos
                            else:
                                print(f"Linea no valida: {linea}") # si alguno de los campos esta vacio, se imprime un mensaje
                        except ValueError:
                            print(f"Linea con formato incorrecto") # si la linea no tiene el formato correcto, se imprime un mensaje
            except Exception as e:
                print(f"Error al cargar los contactos: {e}") # si ocurre un error al abrir el archivo, se imprime un mensaje
        else:
            print("Aun no se han creado Contactos,Ingresa un Contacto.") # si el archivo no existe, se imprime un mensaje indicando que no hay contactos guardados

# Funcion para agregar un contacto
    def agregar_contacto(self, nombre, telefono, correo):
        if not re.match(r"[^@]+@[^@]+\.[^@]+",correo): # esto es una expresion regular para validar el formato del correo, si no es valido no se agrega el contacto
            print("Error: El formato del correo no es valido.")
            return
        nuevo_contacto = Contacto(nombre, telefono, correo) # crea un nuevo objeto Contacto con los datos ingresados 
        self.contactos.append(nuevo_contacto)
        self.guardar_contactos() # llamamos a la funcion guardar_contactos para guardar el contacto
# Funcion para mostrar todos los contactos
    def mostrar_contactos(self):
        if not self.contactos: # si la lista de contactos esta vacia, se imprime un mensaje
            print("No hay contactos guardados")
            return
        for Contacto in self.contactos:
            print(Contacto) # imprime cada contacto en la lista de contactos
# funcion para buscar un contacto por nombre
    def buscar_contacto(self, nombre):
        for Contacto in self.contactos:
            if Contacto.nombre.lower() == nombre.lower(): # compara el nombre ingresado con el nombre de cada contacto en la lista, ignorando mayusculas y minusculas
                print(Contacto) # imprime el contacto encontrado
                return
        print("Contacto no encontrado") # si no se encuentra el contacto, se imprime un mensaje
# Funcion para guardar los contactos
    def guardar_contactos(self):
        try:
            with open(self.archivo, "w", encoding="utf-8") as file: # abre el archivo en modo escritura, si no existe lo crea
                for contacto in self.contactos:
                    file.write(f"{contacto.nombre},{contacto.telefono},{contacto.correo}\n") # escribe cada contacto en el archivo, separando los campos por comas
        except Exception as e:
            print(f"Error al guardar los contactos: {e}") # si ocurre un error al guardar los contactos, se imprime un mensaje de error
# Funcion para eliminar un contacto por nombre
    def eliminar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                self.contactos.remove(contacto) # elimina el contacto de la lista de contactos
                self.guardar_contactos() # llama a la funcion guardar_contactos para guardar los cambios
                print("Contacto eliminado.")
                return
        print("Contacto no encontrado.") 
   
import sys 
sys.stdout.reconfigure(encoding="utf-8")