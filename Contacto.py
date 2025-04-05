class Contacto:
    
    def __init__(self, nombre, telefono, correo):
        
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo

    def __str__(self):
        return f" Nombre: {self.nombre}, Telefono: {self.telefono}, Correo: {self.correo}"