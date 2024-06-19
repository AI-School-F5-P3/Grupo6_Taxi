import time
import logging

# Configuración del logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Taximetro:
    fare_movement = 0.05  # tarifa en movimiento en euros por segundo
    fare_stop = 0.02  # tarifa en reposo en euros por segundo

    def __init__(self):
        self.start_road = False
        self.last_status_change = None
        self.fare_total = 0
        self.in_movement = False
        logging.info("Taxímetro inicializado.")

    def calculate_fare(self):
        now = time.time()
        if self.last_status_change:
            time_elapsed = now - self.last_status_change
            if self.in_movement:
                self.fare_total += time_elapsed * self.fare_movement
            else:
                self.fare_total += time_elapsed * self.fare_stop
        self.last_status_change = now
        logging.info(f"Tarifa actualizada: {self.fare_total:.2f} euros.")

    def start(self):
        logging.info("Carrera iniciada.")
        self.start_road = True
        self.last_status_change = time.time()
        self.calculate_fare()

    def stop(self):
        logging.info("Taxi detenido.")
        self.in_movement = False
        self.calculate_fare()

    def continue_road(self):
        logging.info("Taxi en movimiento.")
        if self.start_road:
            self.in_movement = True
            self.calculate_fare()
        else:
            logging.warning("No se puede continuar la carrera. Primero debe iniciarla.")

    def finish_road(self):
        logging.info("Carrera finalizada.")
        self.calculate_fare()
        logging.info(f"Total a cobrar: {self.fare_total:.2f} euros.")
        return self.fare_total

    def clear(self):
        logging.info("Taxímetro reiniciado.")
        self.start_road = False
        self.last_status_change = None
        self.fare_total = 0
        self.in_movement = False