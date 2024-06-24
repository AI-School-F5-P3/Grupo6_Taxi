import csv




class User:
    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd

class Database:
    def __init__(self, filename):
        self.filename = filename
        self.users = self.load_users()
        
    def add_user(self, name, pwd):
        # Verificar si el usuario ya existe
        for user in self.users:
            if user.name == name:
                print("Nombre de usuario no disponible")
                return False
        new_user = User(name, pwd)
        self.users.append(new_user)
        self.save_users()
        print("Usuario agregado exitosamente.")
        return True

    def authenticate_user(self, name, pwd):
        for user in self.users:
            if user.name == name and user.pwd == pwd:
                return True
        return False

    def save_users(self):
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            for user in self.users:
                writer.writerow([user.name, user.pwd])

    def load_users(self):
        users = []
        try:
            with open(self.filename, mode='r') as file: 
                reader = csv.reader(file)
                for row in reader:
                    if row:
                        users.append(User(row[0], row[1]))
        except FileNotFoundError:
            pass #sino se encuentra el archivo se devuelve la lista vacia
        return users
    
    def authenticate_user(db):
        db = Database('usuarios.csv')

        counter = 3
        while counter > 0:
            n = input("Ingrese su usuario: ")
            p = input("Ingrese su contraseña: ")

        if db.authenticate_user(n, p):
            print(f"{n}, ¡Bienvenido al programa!")
            return True
        else:
            counter -= 1
            print("Usuario o contraseña incorrectos. Intentos restantes:", counter)

        print("Has superado el límite de intentos.")
        return False