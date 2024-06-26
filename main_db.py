<<<<<<< HEAD
import logging
=======
>>>>>>> dev
from Db_psw import Database
from main import main
import getpass

<<<<<<< HEAD
# Configuración de logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename='app.log',
                    filemode='a')
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

if __name__ == "__main__":
    logging.info("Inicio del programa")
    db = Database()  # Crea una instancia de la base de datos
    logging.debug("Instancia de la base de datos creada")

    while True:
=======

if __name__ == "__main__":
    db = Database()  # Crea una instancia de la base de datos

    # Añadir un nuevo usuario (puedes comentar esta línea después de la primera ejecución)
    #db.add_user("admin", "admin123")
while True:
>>>>>>> dev
        print("Seleccione una opción:")
        print("1. Iniciar sesión")
        print("2. Crear un nuevo usuario")
        print("3. Salir")
        option = input("Ingrese su opción (1/2/3): ")

        if option == '1':
<<<<<<< HEAD
            logging.info("Intento de inicio de sesión")
            user = db.authenticate_user_with_limit()
            if user:
                logging.info("Acceso permitido para el usuario")
                print("Acceso permitido.")
                main(user)
                break
            else:
                logging.warning("Acceso denegado para el intento de inicio de sesión")
=======
            user = db.authenticate_user_with_limit()
            if user:
                # Aquí podrías llamar a otras funciones o iniciar otra parte del programa
                print("Acceso permitido.")
                main(user) 
                # Aquí es donde inicia el programa del taxímetro
                break
            else:
>>>>>>> dev
                print("Acceso denegado.")
        elif option == '2':
            name = input("Ingrese el nombre del nuevo usuario: ")
            pwd = getpass.getpass("Ingrese la contraseña del nuevo usuario: ")
<<<<<<< HEAD
            logging.info(f"Creando nuevo usuario: {name}")
            db.add_user(name, pwd)
            logging.debug(f"Usuario {name} añadido exitosamente")
        elif option == '3':
            logging.info("Cerrando la base de datos y terminando el programa")
            db.close()
            print("¡Hasta pronto!")
            break
        else:
            logging.error("Opción no válida ingresada")
            print("Opción no válida. Por favor, intente nuevamente.")

    db.close()  # Asegura que la conexión a la base de datos se cierre correctamente
    logging.info("Programa terminado")
=======
            db.add_user(name, pwd)
        elif option == '3':
            db.close() # Cierra la conexión a la base de datos al final
            print("¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Por favor, intente nuevamente.")

db.close()  # Cierra la conexión a la base de datos al final
>>>>>>> dev
