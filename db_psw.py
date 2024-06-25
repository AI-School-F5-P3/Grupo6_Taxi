import sqlite3

class User:
    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd

class Database:
    def __init__(self, db_filename="usuarios.db"):
        self.db_filename = db_filename
        self.conn = sqlite3.connect(self.db_filename)
        self.create_table()

    def create_table(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL UNIQUE,
                    pwd TEXT NOT NULL
                )
            ''')
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error al crear la tabla: {e}")

    def add_user(self, name, pwd):
        try:
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO users (name, pwd) VALUES (?, ?)", (name, pwd))
            self.conn.commit()
            print("Usuario agregado exitosamente.")
            return True
        except sqlite3.IntegrityError:
            print("El usuario ya existe.")
            return False

    def authenticate_user(self, name, pwd):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM users WHERE name = ? AND pwd = ?", (name, pwd))
        user = cursor.fetchone()
        return user is not None

    def authenticate_user_with_limit(self):
        counter = 3
        while counter > 0:
            n = input("Ingrese su usuario: ")
            p = input("Ingrese su contraseña: ")

            if self.authenticate_user(n, p):
                print(f"{n}, ¡Bienvenido al programa!")
                return True
            else:
                counter -= 1
                print("Usuario o contraseña incorrectos. Intentos restantes:", counter)

        print("Has superado el límite de intentos.")
        return False

    def close(self):
        self.conn.close()

