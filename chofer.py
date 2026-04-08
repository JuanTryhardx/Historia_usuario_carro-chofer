class Chofer:
    def __init__(self, nombre, documento, licencia):
        self._nombre = nombre
        self._documento = documento
        self._licencia = licencia

    # GETTERS
    def get_nombre(self):
        return self._nombre

    def get_documento(self):
        return self._documento

    def get_licencia(self):
        return self._licencia

    # SETTERS
    def set_nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    def set_documento(self, nuevo_doc):
        self._documento = nuevo_doc

    def set_licencia(self, nueva_lic):
        self._licencia = nueva_lic

    def ver_info(self):
        print(f"  Nombre      : {self._nombre}")
        print(f"  Documento   : {self._documento}")
        print(f"  Licencia    : {self._licencia}")