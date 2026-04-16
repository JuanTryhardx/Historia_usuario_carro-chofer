class Base_datos:
    def __init__(self):
        self.lista_info = []

    def guardar_info(self, obj_carro, obj_chofer):
        dato_carro = [
            obj_carro.get_placa(),
            obj_carro.get_modelo(),
            obj_carro.get_color(),
            obj_carro.get_fecha_salida(),
            obj_carro.get_fecha_entrada(),
            obj_carro.get_hora_entrada(),
        ]
        dato_chofer = [
            obj_chofer.get_cedula(),
            obj_chofer.get_nombre(),
            obj_chofer.get_telefono(),
            obj_chofer.get_licencia(),
        ]
        self.lista_info.append([dato_carro, dato_chofer])

    def buscar_info(self):
        pass

    def ver_info(self):
        if not self.lista_info:
            print("No hay registros guardados.")
            return
        
        for indice, registro in enumerate(self.lista_info, 1):
            carro, chofer = registro
            print(f"Registro {indice}:")
            print(f"  Carro - placa: {carro[0]}, modelo: {carro[1]}, color: {carro[2]}, fecha salida: {carro[3]}, fecha entrada: {carro[4]}, hora entrada: {carro[5]}")
            print(f"  Chofer - cédula: {chofer[0]}, nombre: {chofer[1]}, teléfono: {chofer[2]}, licencia: {chofer[3]}")
