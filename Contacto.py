class Contacto:
    
    def __init__(self, nombre, telefono, correo): # constructor de la clase Contacto, recibe el nombre, telefono y correo como parametros
        # inicializa el atributo nombre con el valor recibido
        self.nombre = nombre 
        self.telefono = telefono
        self.correo = correo

    def __str__(self): # metodo para representar el objeto Contacto como una cadena de texto
        return f" Nombre: {self.nombre}, Telefono: {self.telefono}, Correo: {self.correo}"