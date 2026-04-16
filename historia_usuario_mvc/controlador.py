from carro_modelo import Carro
from chofer_modelo import Chofer
from base_datos import Base_datos

class Controlador:
    def __init__(self, obj_vista):
        self.obj_modelo = None
        self.chofer = None
        self.obj_vista = obj_vista
        self.obj_bd = Base_datos()

    def recibir_datos_carro(self):
        datos_carro = self.obj_vista.tomar_datos_carro()
        datos_chofer = self.obj_vista.tomar_datos_chofer()
        self.obj_modelo = Carro(*datos_carro)
        self.chofer = Chofer(*datos_chofer)
        self.obj_bd.guardar_info(self.obj_modelo, self.chofer)

    def confirmar_guardado(self):
        exito = self.obj_modelo is not None and self.chofer is not None
        self.obj_vista.hacer_mensaje(exito)

    def mostrar_registros(self):
        self.obj_vista.visualizar_datos(self.obj_bd.lista_info)
