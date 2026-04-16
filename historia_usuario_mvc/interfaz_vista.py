class Ventana:
    def __init__(self):
        self.titulo = "Registro de Datos"

    def tomar_datos_carro(self):
        placa = input("Digite la placa: ")
        modelo = input("Digite el modelo: ")
        color = input("Digite el color: ")
        fecha_salida = input("Digite la fecha de salida: ")
        fecha_entrada = input("Digite la fecha de entrada: ")
        hora_entrada = input("Digite la hora de entrada: ")
        return [placa, modelo, color, fecha_salida, fecha_entrada, hora_entrada]

    def tomar_datos_chofer(self):
        cedula = input("Digite la cédula del chofer: ")
        nombre = input("Digite el nombre del chofer: ")
        telefono = input("Digite el teléfono del chofer: ")
        licencia = input("Digite la licencia del chofer: ")
        return [cedula, nombre, telefono, licencia]

    def visualizar_datos(self, registros):
        if not registros:
            print("No hay registros para mostrar.")
            return
        print("\nRegistros guardados:")
        for indice, registro in enumerate(registros, 1):
            carro, chofer = registro
            print(f"Registro {indice}:")
            print(f"  Carro - placa: {carro[0]}, modelo: {carro[1]}, color: {carro[2]}, fecha salida: {carro[3]}, fecha entrada: {carro[4]}, hora entrada: {carro[5]}")
            print(f"  Chofer - cédula: {chofer[0]}, nombre: {chofer[1]}, teléfono: {chofer[2]}, licencia: {chofer[3]}")

    def hacer_mensaje(self, exito):
        if exito:
            print("Usuario creado en el sistema")
        else:
            print("ERROR... usuario no creado...")
