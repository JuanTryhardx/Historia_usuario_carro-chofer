class Ventana:
    def __init__(self):
        self.titulo = "Registro de Datos"
        
    def tomar_datos_carro(self):
        placa = input("Digite la placa: ")
        modelo = input("Digite el modelo:: ")
        color = input("Digite el color: ")
        fecha_salida = input("Digite fecha de salida: ")
        fecha_entrada = input("Digite la fecha de entrada: ")
        hora_entrada = input("Digite la hora de entrada: ")
        datos = [placa, modelo, color, fecha_salida, fecha_entrada, hora_entrada]
        return datos
                                 
    def tomar_datos_chofer(self):
        pass
    
    def visualizar_datos(self):
        pass
    