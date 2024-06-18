import time
import datetime


class Taximetro:
    fare_movement = 0.05  # tarifa en movimiento en centimos de euro por segundo
    fare_stop = 0.02 #tarifa en reposo de centimos en euro por segundo
    def __init__(self): 
        self.initial_fare = 0
        self.fare_total = 0 #ira aumentando segun se mueva o este en espera despues de iniciar la carrera
        self.in_movement = False
    def start(self):
        print("start the road trip.")
        self.start_road = True 
        self.fare_total = 0
        self.in_movement = False
        self.calculate_fare()
    def move(self):
        print("The taxi is moving on the road.")
        self.in_movement = True