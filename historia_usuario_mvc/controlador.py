from carro_modelo import Carro
from base_datos import Base_datos

class Controlador:
    def __init__(self, obj_vista):
        self.obj_modelo = " "
        self.obj_vista = obj_vista
        self.obj_bd = Base_datos()
        
    def recibir_datos_carro(self):
        info_datos = self.obj_vista.tomar_datos_carro()
        self.obj_modelo = Carro(info_datos[0], info_datos[1], info_datos[2])
        self.db.guardar_info(self.obj_modelo, self.chofer)
     
    
    
    def confirmar_guardado(self):
        # este true depende de la respuesta de modelo
        self.obj_vista.hacer_mensaje(False)
      
      
      
#El controlador es el unico que consrtruye y guarda los modelos
      
    
    