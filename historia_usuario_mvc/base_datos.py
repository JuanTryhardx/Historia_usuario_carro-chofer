class Base_datos:
    def __init__(self):
        self.lista_info = []
        
    def guardar_info(self, obj_carro):
        dato_carro = [obj_carro.get_placa(), obj_carro.get_modelo()]
        dato_chofer = [obj_chofer.get_cedula(), obj_chofer.get_nombre()]
        datos_totales = [dato_carro, dato_chofer]
        self.lista_info.append(datos_totales)
    
    def buscar_info(self):
        pass
    
    def ver_info(self):
        print("Esta Pendiente por hacer.....")
        for info in self.lista_info:
            print(info)