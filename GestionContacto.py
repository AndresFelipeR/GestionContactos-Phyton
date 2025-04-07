import os
import re
from Contacto import Contacto

class GestionContacto:
    
    def __init__(self,archivo="contactos.txt"):
        self.contactos = []
        self.archivo = archivo
        self.cargar_contactos()

    def cargar_contactos(self):
        if os.path.exists(self.archivo):
            try:
                with open(self.archivo, "r", encoding="utf-8") as file:
                    for linea in file:
                        try:
                            nombre, telefono , correo = linea.strip().split(",")
                            if nombre and telefono and correo:
                                self.contactos.append(Contacto(nombre,telefono,correo))
                            else:
                                print(f"Linea no valida: {linea}")
                        except ValueError:
                            print(f"Linea con formato incorrecto")
            except Exception as e:
                print(f"Error al cargar los contactos: {e}")
        else:
            print("Aun no se han creado Contactos,Ingresa un Contacto.")

    def agregar_contacto(self, nombre, telefono, correo):
        if not re.match(r"[^@]+@[^@]+\.[^@]+",correo):
            print("Error: El formato del correo no es valido.")
            return
        nuevo_contacto = Contacto(nombre, telefono, correo)
        self.contactos.append(nuevo_contacto)
        self.guardar_contactos()

    def mostrar_contactos(self):
        if not self.contactos:
            print("No hay contactos guardados")
            return
        for Contacto in self.contactos:
            print(Contacto)

    def buscar_contacto(self, nombre):
        for Contacto in self.contactos:
            if Contacto.nombre.lower() == nombre.lower():
                print(Contacto)
                return
        print("Contacto no encontrado")

    def guardar_contactos(self):
        try:
            with open(self.archivo, "w", encoding="utf-8") as file:
                for contacto in self.contactos:
                    file.write(f"{contacto.nombre},{contacto.telefono},{contacto.correo}\n")
        except Exception as e:
            print(f"Error al guardar los contactos: {e}")

    def eliminar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                self.contactos.remove(contacto)
                self.guardar_contactos()
                print("Contacto eliminado.")
                return
        print("Contacto no encontrado.") 

    def cargar_contactos(self):
        if not os.path.exists(self.archivo):
            return
        try:
            with open(self.archivo, "r") as file:
                for linea in file:
                    nombre, telefono, correo = linea.strip().split(",")
                    self.contactos.append(Contacto(nombre, telefono, correo))
        except Exception as e:
            print(f"Error al cargar los contactos: {e}")

import sys
sys.stdout.reconfigure(encoding="utf-8")