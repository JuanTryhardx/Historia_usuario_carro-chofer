from carro import Carro
from chofer import Chofer
from base_datos import Base_datos

# Crear base de datos
bd = Base_datos()


print("\n--- REGISTRAR ENTRADA ---")
c1 = Carro("ABC123", "Toyota Corolla", "Blanco")
c2 = Carro("XYZ789", "Chevrolet Spark", "Rojo")
c3 = Carro("DEF456", "Renault Logan", "Gris")

bd.registrar_entrada(c1)   
bd.registrar_entrada(c2)  
bd.registrar_entrada(c3)   


print("\n--- ASIGNAR CHOFERES ---")
ch1 = Chofer("Carlos Pérez",   "1023456789", "LIC-001")
ch2 = Chofer("María González", "9876543210", "LIC-002")

bd.asignar_chofer(0, ch1)
bd.asignar_chofer(1, ch2)


print("\n--- VER TODOS ---")
bd.ver_todos()


print("\n--- BUSCAR POR PLACA ---")
bd.buscar_por_placa("XYZ789")


print("\n--- REGISTRAR SALIDA ---")
bd.registrar_salida(0)


print("\n--- ELIMINAR REGISTRO ---")
bd.eliminar_registro(2)

print("\n--- REGISTRO FINAL ---")
bd.ver_todos()