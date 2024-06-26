import time
from datetime import datetime
from fare_ondemand import calculate_peak_fare
from logger import log_info, log_warning, log_error  # Importa las funciones de logging

class Taximetro:
    fare_movement = 0.05  # tarifa en movimiento en centimos de euro por segundo
    fare_stop = 0.02  # tarifa en reposo de centimos en euro por segundo

    def __init__(self):
        self.start_road = False
        self.last_status_change = None
        self.fare_total = 0  # ira aumentando segun se mueva o este en espera despues de iniciar la carrera
        self.in_movement = False
        self.start_time = None
        self.end_time = None
        log_info("Taxímetro inicializado.")  # Log de inicialización

    def calculate_fare(self):
        now = time.time()
        if self.last_status_change is not None:
            time_elapsed = now - self.last_status_change
            fare = calculate_peak_fare(self.in_movement)
            self.fare_total += round(time_elapsed * fare, 2)
        self.last_status_change = now
        log_info(f"Tarifa calculada: {self.fare_total:.2f} euros.")  # Log de tarifa calculada

    def start(self):
        print("Comenzar la carrera.")
        self.start_road = True
        self.last_status_change = time.time()
        self.start_time = datetime.now()  # Guarda la fecha y hora de inicio
        log_info(f"Carrera iniciada a las {self.start_time}.")  # Log de inicio de carrera

    def stop(self):
        print("El taxi se ha detenido.")
        self.calculate_fare()
        self.in_movement = False
        log_info("Taxi detenido.")  # Log de taxi detenido

    def continue_road(self):
        if self.start_road:
            self.calculate_fare()
            self.in_movement = True
            print(f"El taxi esta en movimiento.")
            log_info("Taxi en movimiento.")  # Log de taxi en movimiento

    def finish_road(self):
        self.calculate_fare()
        self.start_road = False
        self.end_time = datetime.now()  # Guarda la fecha y hora de finalización
        print(f"La carrera ha terminado. El total a cobrar es: {self.fare_total:.2f} euros.")
        self.save_ride_history()
        log_info(f"Carrera finalizada a las {self.end_time}. Total: {self.fare_total:.2f} euros.")  # Log de carrera finalizada
        return self.fare_total

    def save_ride_history(self):
        with open('rides_history.txt', mode='a', encoding='utf-8') as file:
            file.write(f"Fecha de inicio: {self.start_time}\n")
            file.write(f"Fecha de fin: {self.end_time}\n")
            file.write(f"Total a cobrar: €{self.fare_total:.2f}\n")
            file.write("=======================================\n")
        log_info("Historial de carrera guardado.")  # Log de guardado de historial

    def view_history(self):
        try:
            with open('rides_history.txt', mode='r', encoding='utf-8') as file:
                print(f"Historial de carreras:")
                for line in file:
                    print(line.strip())
            log_info("Historial de carreras visualizado.")  # Log de visualización de historial
        except FileNotFoundError:
            log_warning("No hay carreras registradas.")  # Log de historial no encontrado
            print("No hay carreras registradas.")

    def clear(self):
        self.start_road = False
        self.last_status_change = None
        self.fare_total = 0
        self.in_movement = False
        self.start_time = None
        self.end_time = None
        log_info("Taxímetro reiniciado.")  # Log de reinicio de taxímetro

