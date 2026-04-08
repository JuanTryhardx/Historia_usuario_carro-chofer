from carro import Carro
from chofer import Chofer
from base_datos import Base_datos

# Crear base de datos
bd = Base_datos()

# ── CREATE: registrar entrada de carros ──────────────
print("\n--- REGISTRAR ENTRADA ---")
c1 = Carro("ABC123", "Toyota Corolla", "Blanco")
c2 = Carro("XYZ789", "Chevrolet Spark", "Rojo")
c3 = Carro("DEF456", "Renault Logan", "Gris")

bd.registrar_entrada(c1)   # posición 0
bd.registrar_entrada(c2)   # posición 1
bd.registrar_entrada(c3)   # posición 2

# ── UPDATE: asignar choferes ─────────────────────────
print("\n--- ASIGNAR CHOFERES ---")
ch1 = Chofer("Carlos Pérez",   "1023456789", "LIC-001")
ch2 = Chofer("María González", "9876543210", "LIC-002")

bd.asignar_chofer(0, ch1)
bd.asignar_chofer(1, ch2)

# ── READ: ver todos los registros ───────────────────
print("\n--- VER TODOS ---")
bd.ver_todos()

# ── READ: buscar por placa ───────────────────────────
print("\n--- BUSCAR POR PLACA ---")
bd.buscar_por_placa("XYZ789")

# ── UPDATE: registrar salida ─────────────────────────
print("\n--- REGISTRAR SALIDA ---")
bd.registrar_salida(0)

# ── DELETE: eliminar un registro ─────────────────────
print("\n--- ELIMINAR REGISTRO ---")
bd.eliminar_registro(2)

# ── READ final ───────────────────────────────────────
print("\n--- REGISTRO FINAL ---")
bd.ver_todos()