from base_datos

obj_vista = Ventana()
obj_controlador = Controlador(obj_vista)

obj_controlador.recibir_datos_carro()

obj_db = Base_datos()
obj_db.ver_info()