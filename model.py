import logging
import time

class Taximetro:
    fare_movement = 0.05  # tarifa en movimiento en centimos de euro por segundo
    fare_stop = 0.02  # tarifa en reposo de centimos en euro por segundo

    def __init__(self):
        self.start_road = False
        self.last_status_change = None
        self.fare_total = 0  # ira aumentando segun se mueva o este en espera despues de iniciar la carrera
        self.in_movement = False
        logging.info("Taximetro inicializado.")

    def calculate_fare(self):
        now = time.time()
        time_elapsed = now - self.last_status_change
        if self.in_movement:
            self.fare_total += round(time_elapsed * self.fare_stop, 2)
            logging.info(f"Calculando tarifa en reposo: {self.fare_total}")
        else:
            self.fare_total += round(time_elapsed * self.fare_movement, 2)
            logging.info(f"Calculando tarifa en movimiento: {self.fare_total}")
        self.last_status_change = now

    def start(self):
        logging.info("Comenzar la carrera.")
        self.start_road = True
        self.last_status_change = time.time()

    def stop(self):
        logging.info("El taxi se ha detenido.")
        self.in_movement = False
        self.calculate_fare()

    def continue_road(self):
        if self.start_road:
            self.in_movement = True
            self.calculate_fare()
            logging.info("El taxi esta en movimiento.")

    def finish_road(self):
        self.in_movement = not self.in_movement
        self.calculate_fare()
        self.start_road = False
        logging.info(f"La carrera ha terminado. El total a cobrar es: {self.fare_total:.2f} euros.")
        return self.fare_total

    def clear(self):
        self.last_status_change = None
        self.fare_total = 0
        self.in_movement = False
        logging.info("Taximetro reiniciado.")