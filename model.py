import time
from datetime import datetime
from fare_ondemand import calculate_peak_fare
from Db_psw import Database
import logging

# Configuración de logging
logging.basicConfig(filename='taximetro.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

class Taximetro:
    fare_movement = 0.05  # tarifa en movimiento en centimos de euro por segundo
    fare_stop = 0.02  # tarifa en reposo de centimos en euro por segundo

    def __init__(self, user):
        self.start_road = False
        self.last_status_change = None
        self.fare_total = 0
        self.in_movement = False
        self.start_time = None
        self.end_time = None
        self.user = user[0]
        logging.info(f"Taximetro inicializado para el usuario {self.user}")

    def calculate_fare(self):
        now = time.time()
        if self.last_status_change is not None:
            time_elapsed = now - self.last_status_change
            fare = calculate_peak_fare(self.in_movement)
            self.fare_total += round(time_elapsed * fare, 2)
        self.last_status_change = now

    def start(self):
        self.start_road = True
        self.last_status_change = time.time()
        self.start_time = datetime.now()
        logging.info("Comenzar la carrera.")
        print("Comenzar la carrera.")

    def stop(self):
        if self.in_movement:
            self.calculate_fare()
            self.in_movement = False
            logging.info("El taxi se ha detenido.")
            print("El taxi se ha detenido.")
        else:
            print("Inicie el movimiento")

    def continue_road(self):
        if self.start_road and self.in_movement == False:
            self.calculate_fare()
            self.in_movement = True
            logging.info("El taxi está en movimiento.")
            print("El taxi está en movimiento.")
        else:
            print("El taxi ya esta en movimiento.")

    def finish_road(self):
        if self.start_road:
            self.calculate_fare()
            self.start_road = False
            self.end_time = datetime.now()
            logging.info(f"La carrera ha terminado. El total a cobrar es: {self.fare_total:.2f} euros.")
            print(f"\033[32mLa carrera ha terminado. El total a cobrar es: {self.fare_total:.2f} euros.\033[0m")
            self.save_ride_history()
            db = Database()
            db.add_trip_database(self.start_time, self.end_time, round(self.fare_total,2), self.user)
            return self.fare_total
        else:
            print("La carrera no ha sido iniciada")

    def save_ride_history(self):
        with open('rides_history.txt', mode='a', encoding='utf-8') as file:
            file.write(f"Fecha de inicio: {self.start_time}\n")
            file.write(f"Fecha de fin: {self.end_time}\n")
            file.write(f"Total a cobrar: €{self.fare_total:.2f}\n")
            file.write("=======================================\n")
        logging.info("Historial de viaje guardado.")

    def get_history(self):
        history = []
        try:
            with open('rides_history.txt', mode='r', encoding='utf-8') as file:
                current_trip = {}
                for line in file:
                    if line.startswith("Fecha de inicio"):
                        current_trip['start'] = line.split(": ")[1].strip()
                    elif line.startswith("Fecha de fin"):
                        current_trip['end'] = line.split(": ")[1].strip()
                    elif line.startswith("Total a cobrar"):
                        current_trip['fare'] = line.split(": €")[1].strip()
                    elif line.startswith("="):
                        history.append(current_trip)
                        current_trip = {}
            logging.info("Historial de carreras recuperado.")
        except FileNotFoundError:
            logging.warning("Intento de recuperar historial fallido: archivo no encontrado.")
        return history

    def view_history(self):
        try:
            with open('rides_history.txt', mode='r', encoding='utf-8') as file:
                print("Historial de carreras:")
                for line in file:
                    print(line.strip())
            logging.info("Historial de carreras visualizado.")
        except FileNotFoundError:
            print("No hay carreras registradas.")
            logging.warning("Intento de visualizar historial fallido: archivo no encontrado.")

    def history_db(self):
        db = Database()
        history = db.show_history(self.user)
        print("# | Hora de inicio\t\t| Hora de fin\t\t\t| Total")
        print("-"*70)
        i = 1
        for history in history:
            print(f"{i} | {history[0]}  | {history[1]}\t| {history[2]}")
            print("-"*70)
            i += 1
        logging.info("Historial de la base de datos visualizado.")

    def clear(self):
        self.start_road = False
        self.last_status_change = None
        self.fare_total = 0
        self.in_movement = False
        self.start_time = None
        self.end_time = None
        logging.info("Datos del taxímetro reiniciados.")