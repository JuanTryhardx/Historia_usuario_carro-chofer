class Chofer:
    def __init__(self, cedula, nombre, telefono, licencia):
        self.cedula = cedula
        self.nombre = nombre
        self.telefono = telefono
        self.licencia = licencia

    def get_cedula(self):
        return self.cedula

    def set_cedula(self, nueva_cedula):
        self.cedula = nueva_cedula

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def get_telefono(self):
        return self.telefono

    def set_telefono(self, nuevo_telefono):
        self.telefono = nuevo_telefono

    def get_licencia(self):
        return self.licencia

    def set_licencia(self, nueva_licencia):
        self.licencia = nueva_licencia

    def ver_info(self):
        return f"Cédula: {self.cedula} - Nombre: {self.nombre} - Teléfono: {self.telefono} - Licencia: {self.licencia}"
