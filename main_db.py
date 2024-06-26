import logging
from Db_psw import Database
from main import main
import getpass

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
        print("Seleccione una opción:")
        print("1. Iniciar sesión")
        print("2. Crear un nuevo usuario")
        print("3. Salir")
        option = input("Ingrese su opción (1/2/3): ")

        if option == '1':
            logging.info("Intento de inicio de sesión")
            user = db.authenticate_user_with_limit()
            if user:
                logging.info("Acceso permitido para el usuario")
                print("Acceso permitido.")
                main(user)
                break
            else:
                logging.warning("Acceso denegado para el intento de inicio de sesión")
                print("Acceso denegado.")
        elif option == '2':
            name = input("Ingrese el nombre del nuevo usuario: ")
            pwd = getpass.getpass("Ingrese la contraseña del nuevo usuario: ")
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