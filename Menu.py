from GestionContacto import GestionContacto
#Menu principal
def menu():
    gestion = GestionContacto()

    while True:
        print("\n--- Sistema de Gestion de Contactos ---")
        print("1. Agregar un Contacto")
        print("2. Mostrar todos los contactos")
        print("3. Buscar un Contacto")
        print("4. Eliminar un Contacto")
        print("5. Salir")

        
        opcion = input("Selecione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre: ")
            telefono = input("Ingrese el teléfono: ")
            correo = input("Ingrese el correo electrónico: ")
            gestion.agregar_contacto(nombre, telefono, correo)
        elif opcion == "2":
            gestion.mostrar_contactos()
        elif opcion == "3":
            nombre = input("Ingrese el nombre del contacto a buscar: ")
            gestion.buscar_contacto(nombre)
        elif opcion == "4":
            nombre = input("Ingrese el nombre del contacto a eliminar: ")
            gestion.eliminar_contacto(nombre)
        elif opcion == "5":
            print("¡Hasta Pronto!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    menu()