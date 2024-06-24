from model import Taximetro
import time
from db_psw import authenticate_user

# Programa principal
if __name__ == "__main__":
    if authenticate_user():
        taximetro = Taximetro()
        while True:
            print("\n¿Qué acción desea realizar?")
            print("1. Comenzar carrera")
            print("2. Continuar en la carrera")
            print("3. Detener el taxi")
            print("4. Terminar la carrera")
            print("5. Ver historial de carreras")
            print("6. Salir del programa")

            opcion = input("Ingrese el número de la acción: ")

            if opcion == "1":
                taximetro.start()
            elif opcion == "2":
                taximetro.continue_road()
            elif opcion == "3":
                taximetro.stop()
            elif opcion == "4":
                taximetro.finish_road()
            elif opcion == "5":
                taximetro.view_history()
            elif opcion == "6":
                print("Saliendo del programa...")
                break
            else:
                print("Opción inválida. Por favor, ingrese un número válido.")
    else:
        print("No se pudo autenticar. Saliendo del programa...")