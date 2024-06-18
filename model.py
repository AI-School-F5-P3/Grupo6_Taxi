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


    def start(self):
        print("Comenzar la carrera.")
        self.start_road = True 
        self.fare_total = 0


    def stop(self):
        print("Taxi stopped.")
        self.in_movement = False


    def continue_road(self, in_movement):
        now = time.time()
        if self.last_status_change is not None:
            time_elapsed = now - self.last_status_change
            if self.in_movement:
                self.fare_total += time_elapsed * self.fare_movement
            else:
                self.fare_total += time_elapsed * self.fare_stop
        
        self.in_movement = in_movement
        self.last_status_change = now
        estado = "movimiento" if in_movement else "parado"
        print(f"El taxi esta {estado}.")
    
    def finish_road(self):
        self.finish_road = time.time()
        time_elapsed = self.finish_road - self.last_status_change
        if self.in_movement:
            self.total += time_elapsed * self.fare_movement
        else:
            self.total += time_elapsed * self.fare_stopped
        print(f"La carrera ha terminado. El total a cobrar es: {self.total:.2f} euros.")
        return self.total
    
    def clear(self):
        self.start_road = True
        self.last_status_change= None
        self.fare_total = 0
        self.in_movement = False