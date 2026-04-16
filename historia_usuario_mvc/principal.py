from base_datos import Base_datos
from controlador import Controlador
from interfaz_vista import Ventana

obj_vista = Ventana()
obj_controlador = Controlador(obj_vista)

obj_controlador.recibir_datos_carro()
obj_controlador.confirmar_guardado()

obj_db = Base_datos()
obj_db.ver_info()