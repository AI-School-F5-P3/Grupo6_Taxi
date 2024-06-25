from model import Taximetro
import time

#Función main():
#Crea una instancia de la clase Taximetro.
#Imprime las instrucciones para el usuario.
#Entra en un bucle infinito para leer comandos del usuario y llamar a los métodos correspondientes del taxímetro.
def main(user):
    taximetro = Taximetro(user)

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
            taximetro.history_db()
        elif comando == "X":
            print("Gracias por usar nuestro taximetro. ")
            break
        else:
            print("Comando inválido. Intente de nuevo.")
    


if __name__ == "__main__":
    main()