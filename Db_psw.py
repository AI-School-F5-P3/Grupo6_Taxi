import sqlite3
import bcrypt
import getpass



#se define la clase User, con los atributos, name y pwd que corresponden a nombre y contraseña
class User:
    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd

#se define la clase Database con los atributos db_filename
class Database:
    def __init__(self, db_filename="taximetro.db"):
        self.db_filename = db_filename
        self.conn = sqlite3.connect(self.db_filename)
        self.create_table()

#funcion para crear tablas dentro del archivo taximetro.db
    def create_table(self):
        try:
            cursor = self.conn.cursor()
            querys = [
                '''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL UNIQUE,
                    pwd TEXT NOT NULL
                );
            ''',
            '''
                CREATE TABLE IF NOT EXISTS trips (
				id INTEGER PRIMARY KEY,
                user_id INTEGER NOT NULL,
                begin_date TEXT,
                end_date TEXT,
                total REAL,
                FOREIGN KEY (user_id) REFERENCES users (id)
			    );
            '''
            ]
            for q in querys:
                cursor.execute(q)
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error al crear la tabla: {e}")
#se crea a funcion de añadir usuario con atributos y usando el bcrypt para hashear la contraseña en la base de datos
    def add_user(self, name, pwd):
        hashed_pwd = bcrypt.hashpw(pwd.encode('utf-8'), bcrypt.gensalt())
        try:
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO users (name, pwd) VALUES (?, ?)", (name, hashed_pwd.decode('utf-8')))
            self.conn.commit()
            print("Usuario agregado exitosamente.")
            return True
        except sqlite3.IntegrityError:
            print("El usuario ya existe.")
            return False
#se define al funcion de autenticar usuario
    def authenticate_user(self, name, pwd):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM users WHERE name = ?", (name,))
        result = cursor.fetchone()
        if result:
            stored_pwd = result[2] #pwd esta en el indice 2
            if  bcrypt.checkpw(pwd.encode('utf-8'), stored_pwd.encode('utf-8')):
                return result
        return None
#se define la funcion para intentar autenticar un usuario con contraseña, en este caso 3 veces.
    def authenticate_user_with_limit(self):
        counter = 3
        while counter > 0:
            n = input("Ingrese su usuario: ")
            p = getpass.getpass("Ingrese su contraseña: ")
            user = self.authenticate_user(n, p)
            if user != None:
                print(f"{n}, ¡Bienvenido al programa!")
                return user
            else:
                counter -= 1
                print("Usuario o contraseña incorrectos. Intentos restantes:", counter)

        print("Has superado el límite de intentos.")
        return 0

#se define la funcion para agregar los datos del viaje a la base de datos 
    def add_trip_database(self, start_time, end_time, total, user):
        cursor = self.conn.cursor()
        query = """INSERT INTO 
                trips(begin_date, end_date, total, user_id) 
                VALUES(?, ?, ?, ?)"""
        cursor.execute(query, (start_time, end_time, total, user))
        self.conn.commit()

#se define la funcion para mostrar el historial de la base de datos
    def show_history(self, user_id):
        cursor = self.conn.cursor()
        query = """SELECT begin_date, end_date, total 
                FROM trips 
                WHERE user_id = ?"""
        cursor.execute(query, (user_id, ))
        rows = cursor.fetchall()
        for row in rows:
            print(row)

#se define la funcion para cerrar la conexión actual con la base de datos SQLite.
    def close(self):
        self.conn.close()