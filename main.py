import logging
from model import Taximetro
import time

logging.basicConfig(filename='taximetro.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')


def main():
    logging.info("Inicio del programa Taximetro Digital.")
    taximetro = Taximetro()

    print("Bienvenido al Taxímetro Digital!")
    print('''Estos son los comandos disponibles: 
          - empezar
          - parar
          - continuar
          - finalizar
            con ellos puede usar el programa.\n''')

    while True:
        comando = input("Ingrese un comando: ")
        if comando == "empezar":
            taximetro.start()
        elif comando == "parar":
            taximetro.stop()
        elif comando == "continuar":
            taximetro.continue_road()
        elif comando == "finalizar":
            taximetro.finish_road()
            taximetro.clear()
        else:
            print("Comando inválido. Intente de nuevo.")
            logging.warning("Comando inválido ingresado.")

if __name__ == "__main__":
    main()