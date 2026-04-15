from datetime import datetime

class Base_datos:

    def __init__(self):
        self.lista_carros = []  

  
    def registrar_entrada(self, carro):
        self.lista_carros.append(carro)
        print(f" Carro {carro.get_placa()} registrado en posición {len(self.lista_carros) - 1}")

   
    def asignar_chofer(self, indice, chofer):
        carro = self.buscar_carro(indice)
        if carro:
            carro.set_chofer(chofer)
            print(f" Chofer '{chofer.get_nombre()}' asignado al carro en posición {indice}")

  
    def registrar_salida(self, indice):
        carro = self.buscar_carro(indice)
        if carro:
            fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            carro.set_fecha_salida(fecha)
            print(f" Salida registrada para carro en posición {indice}: {fecha}")

    def ver_todos(self):
        if not self.lista_carros:
            print("  No hay carros registrados.")
            return
        print("\n ====== REGISTRO DE CARROS ======")
        for i in range(len(self.lista_carros)):
            print(f"\n Posición: {i}")
            self.lista_carros[i].ver_info()
        print("===================================\n")

  
    def buscar_carro(self, indice):
        if 0 <= indice < len(self.lista_carros):
            print(f"\n Carro en posición {indice}:")
            self.lista_carros[indice].ver_info()
            return self.lista_carros[indice]
        else:
            print(f" No existe carro en posición {indice}")
            return None

    def buscar_por_placa(self, placa):
        print(f"\n Buscando placa: {placa}")
        encontrado = False
        for i in range(len(self.lista_carros)):
            if self.lista_carros[i].get_placa() == placa:
                self.lista_carros[i].ver_info()
                encontrado = True
        if not encontrado:
            print(f" No se encontró ningún carro con placa {placa}")

   
    def eliminar_registro(self, indice):
        if 0 <= indice < len(self.lista_carros):
            self.lista_carros.pop(indice)
            print(f"  Registro en posición {indice} eliminado.")
        else:
            print(f" No existe registro en posición {indice}")