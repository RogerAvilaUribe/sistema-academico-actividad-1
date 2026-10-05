class persona:
    def __init__(self, nombre, identificacion, correo):
        self.nombre = nombre
        self.identificacion = identificacion
        self.correo = correo

    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}, Identificación: {self.identificacion}, Correo: {self.correo}"