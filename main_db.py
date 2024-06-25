'''en la main del programa taximetro se debe agregar esta main para que 
 inicie el programa si es correcto el usuario y contraseña
 '''

from Db_psw import Database
from model import Taximetro
import time
from Db_psw import User
from main import main


if __name__ == "__main__":
    db = Database()  # Crea una instancia de la base de datos

    # Añadir un nuevo usuario (puedes comentar esta línea después de la primera ejecución)
    #db.add_user("admin", "admin123")
while True:
        print("Seleccione una opción:")
        print("1. Iniciar sesión")
        print("2. Crear un nuevo usuario")
        print("3. Salir")
        option = input("Ingrese su opción (1/2/3): ")

        if option == '1':
            if db.authenticate_user_with_limit():
                # Aquí podrías llamar a otras funciones o iniciar otra parte del programa
                print("Acceso permitido.")
                main() 
                # Aquí es donde inicia el programa del taxímetro
                break
            else:
                print("Acceso denegado.")
        elif option == '2':
            name = input("Ingrese el nombre del nuevo usuario: ")
            pwd = input("Ingrese la contraseña del nuevo usuario: ")
            db.add_user(name, pwd)
        elif option == '3':
            break
        else:
            print("Opción no válida. Por favor, intente nuevamente.")

db.close()  # Cierra la conexión a la base de datos al final