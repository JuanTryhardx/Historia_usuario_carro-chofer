from carro_modelo import Carro
from controlador import Controlador

class Controlador:
    def __init__(obj_modelo, obj_vista):
        self.obj_modelo = " "
        self.obj_vista = obj_vista
        
    def recibir_datos(self):
      info_datos = self.obj_vista.tomar_datos_carro()
      print(info_datos)
      self.obj_modelo = Carro(info_datos[0], info_datos[1] , info_datos[2])
      print(self.obj_modelo.ver_info())
     
      
      
      #El controlador es el unico que consrtruye y guarda los modelos
      
    
    