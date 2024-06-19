import time
import datetime


class Taximetro:
    fare_movement = 0.05  # tarifa en movimiento en centimos de euro por segundo
    fare_stop = 0.02 #tarifa en reposo de centimos en euro por segundo
    def __init__(self):
        self.start_road = True
        self.last_status_change= None
        self.initial_fare = 0
        self.fare_total = 0 #ira aumentando segun se mueva o este en espera despues de iniciar la carrera
        self.in_movement = False
    def calculate_fare(self):
            time_elapsed = time.time() - self.last_status_change
            if self.in_movement:
                self.fare_total += time_elapsed * self.fare_movement
            else:
                self.fare_total += time_elapsed * self.fare_stop

    def start(self):
        print("Comenzar la carrera.")
        self.start_road = True 
        self.fare_total = 0
        self.in_movement = False
        self.calculate_fare()
    def move(self):
        print("El taxi inicio la carrera.")
        self.in_movement = True
    def stop(self):
        print("El taxi se ha detenido. ")
        self.in_movement = False
        self.calculate_fare()

    def continue_road(self):
        now = time.time()
        self.in_movement = True
        if self.last_status_change is not None:
            time_elapsed = now - self.last_status_change
            if self.in_movement:
                self.fare_total += time_elapsed * self.fare_movement
            else:
                self.fare_total += time_elapsed * self.fare_stop
        self.last_status_change = now
        # estado = "movimiento" if in_movement else "parado"
        print(f"El taxi esta en movimiento.")
    
    def finish_road(self):
        time_elapsed = time.time() - self.last_status_change
        if self.in_movement:
            self.fare_total += time_elapsed * self.fare_movement
        else:
            self.fare_total+= time_elapsed * self.fare_stop
        print(f"La carrera ha terminado. El total a cobrar es: {self.fare_total:.2f} euros.")
        return self.fare_total
    
    def clear(self):
        self.start_road = True
        self.last_status_change= None
        self.fare_total = 0
        self.in_movement = False


       