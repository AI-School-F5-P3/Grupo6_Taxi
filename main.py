from model import Taximetro
import time
from logger import log_info, log_warning, log_error  # Importa las funciones de logging

#Función main():
#Crea una instancia de la clase Taximetro.
#Imprime las instrucciones para el usuario.
#Entra en un bucle infinito para leer comandos del usuario y llamar a los métodos correspondientes del taxímetro.
def main(user):
    taximetro = Taximetro(user)

    print("Bienvenido al Taxímetro Digital!")
    log_info("Programa iniciado.")  # Log de inicio del programa
    print('''Estos son los comandos disponibles: 
          - "E" para empezar 
          - "P" para parar 
          - "C" para continuar
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
            taximetro.history_db()
        elif comando == "X":
            print("Gracias por usar nuestro taximetro.")
            log_info("Programa terminado por el usuario.")  # Log de fin del programa
            break
        else:
            print("Comando inválido. Intente de nuevo.")
            log_warning("Comando inválido ingresado.")  # Log de comando inválido

if __name__ == "__main__":
    main()