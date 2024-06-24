import logging
from model import Taximetro
import time

logging.basicConfig(filename='taximetro.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')


def main():
    logging.info("Inicio del programa Taximetro Digital.")
    taximetro = Taximetro()

    print("Bienvenido al Taxímetro Digital!")
    print('''Estos son los comandos disponibles: 
          - "E" para empezar 
          - "P" para parar 
          - "C" continuar
          - "F" para finalizar
          - "H" para visualizar el Historial
          - "X" para salir
            con ellos puede usar el programa.\n''')

    while True:
        comando = input("Ingrese un comando: ").upper()
        if comando == "E":
            taximetro.start()
        elif comando == "P":
            taximetro.stop()
        elif comando == "C":
            taximetro.continue_road()
        elif comando == "F":
            taximetro.finish_road()
            taximetro.clear()
        elif comando == "H":
            taximetro.view_history()
        elif comando == "X":
            print("Gracias por usar nuestro taximetro. ")
            break
        else:
            print("Comando inválido. Intente de nuevo.")
    


if __name__ == "__main__":
    main()