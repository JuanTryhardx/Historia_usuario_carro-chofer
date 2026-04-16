from controlador import Controlador
from interfaz_vista import Ventana


def main():
    obj_vista = Ventana()
    obj_controlador = Controlador(obj_vista)

    while True:
        obj_controlador.recibir_datos_carro()
        obj_controlador.confirmar_guardado()

        opcion = input("¿Deseas registrar otro? (s/n): ").strip().lower()
        if opcion != "s":
            break

    obj_controlador.mostrar_registros()


if __name__ == "__main__":
    main()
