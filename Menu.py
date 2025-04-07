from GestionContacto import GestionContacto # Importamos la clase GestionContacto
#Menu principal
def menu():
    gestion = GestionContacto() # Creamos una instancia de la clase GestionContacto

    while True: # Bucle infinito para mostrar el menu hasta que el usuario decida salir
        ## Mostramos el menu de opciones al usuario
        print("\n--- Sistema de Gestion de Contactos ---")
        print("1. Agregar un Contacto")
        print("2. Mostrar todos los contactos")
        print("3. Buscar un Contacto")
        print("4. Eliminar un Contacto")
        print("5. Salir")

        ## Pedimos al usuario que seleccione una opcion
        opcion = input("Selecione una opción: ")

        ## Ejecutamos la opcion seleccionada
        if opcion == "1":
            nombre = input("Ingrese el nombre: ")
            telefono = input("Ingrese el teléfono: ")
            correo = input("Ingrese el correo electrónico: ")
            gestion.agregar_contacto(nombre, telefono, correo)  # Llamamos a la funcion agregar_contacto para agregar un nuevo contacto, con los datos ingresados por el usuario
        elif opcion == "2":
            gestion.mostrar_contactos() # Llamamos a la funcion mostrar_contactos para mostrar todos los contactos guardados
        elif opcion == "3":
            nombre = input("Ingrese el nombre del contacto a buscar: ")
            gestion.buscar_contacto(nombre) # Llamamos a la funcion buscar_contacto para buscar un contacto por su nombre, con el nombre ingresado por el usuario
        elif opcion == "4":
            nombre = input("Ingrese el nombre del contacto a eliminar: ")
            gestion.eliminar_contacto(nombre) # Llamamos a la funcion eliminar_contacto para eliminar un contacto por su nombre, con el nombre ingresado por el usuario
        elif opcion == "5":
            print("¡Hasta Pronto!") # Mensaje de despedida al salir del programa
            break # Salimos del bucle y terminamos el programa
        else:
            print("Opción no válida. Por favor, intente de nuevo.") # Mensaje de error si la opcion ingresada no es valida

if __name__ == "__main__": # Si este archivo es ejecutado directamente, llamamos a la funcion menu para iniciar el programa
    menu() 