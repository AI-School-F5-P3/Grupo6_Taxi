from db_psw import Database
from db_psw import User


# Programa principal
if __name__ == "__main__":
    filename = "usuarios.csv"
    db = Database(filename)
    

    # Autenticar usuarios y agregarlos a la base de datos
    while True:
        if Database.authenticate_user_2(db):
            while True:
                option = input("¿Desea agregar otro usuario? (y/n): ").lower()
                if option == 'y':
                    name = input("Ingrese el nombre del usuario: ")
                    pwd = input("Ingrese la contraseña del usuario: ")
                    db.add_user(name, pwd)
                elif option == 'n':
                    break
                else:
                    print("Opción no válida. Intente de nuevo.")
            break
        else:
            option = input("¿Desea intentar nuevamente? (s/n): ").lower()
            if option != 's':
                break

    # Mostrar usuarios en la base de datos (opcional)
    print("Usuarios en la base de datos:")
    for user in db.users:
        print(f"Nombre: {user.name}, Contraseña: {user.pwd}")

    # Guardar usuarios en un archivo (opcional)
    filename = 'usuarios.csv'  # Nombre del archivo donde se guardarán los usuarios
    db.save_users()
    print(f"Usuarios guardados en el archivo {filename}.")