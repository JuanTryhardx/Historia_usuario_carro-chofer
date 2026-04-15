from datetime import datetime

class Carro:
    def __init__(self, placa, modelo, color):
        self._placa = placa
        self._modelo = modelo
        self._color = color
        self._fecha_entrada = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._fecha_salida = None
        self._chofer = None

    # GETTERS
    def get_placa(self):
        return self._placa

    def get_modelo(self):
        return self._modelo

    def get_color(self):
        return self._color

    def get_fecha_entrada(self):
        return self._fecha_entrada

    def get_fecha_salida(self):
        return self._fecha_salida

    def get_chofer(self):
        return self._chofer

    # SETTERS
    def set_placa(self, nueva_placa):
        self._placa = nueva_placa

    def set_modelo(self, nuevo_modelo):
        self._modelo = nuevo_modelo

    def set_color(self, nuevo_color):
        self._color = nuevo_color

    def set_fecha_salida(self, fecha):
        self._fecha_salida = fecha

    def set_chofer(self, chofer):
        self._chofer = chofer

    def ver_info(self):
        print(f"  Placa       : {self._placa}")
        print(f"  Modelo      : {self._modelo}")
        print(f"  Color       : {self._color}")
        print(f"  Entrada     : {self._fecha_entrada}")
        print(f"  Salida      : {self._fecha_salida if self._fecha_salida else 'Aún en instalaciones'}")
        if self._chofer:
            print(f"  --- Chofer asignado ---")
            self._chofer.ver_info()
        else:
            print(f"  Chofer      : Sin asignar")