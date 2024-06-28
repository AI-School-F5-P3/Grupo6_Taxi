import time
from datetime import datetime
from fare_ondemand import calculate_peak_fare
from Db_psw import Database
import logging

# Configuración de logging
logging.basicConfig(filename='taximetro.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')



 #se define la clase taximetro
class Taximetro:
    fare_movement = 0.05  # tarifa en movimiento en centimos de euro por segundo
    fare_stop = 0.02  # tarifa en reposo de centimos en euro por segundo

#se inicializan los objetos de la clase Taximetro con sus atributo
    def __init__(self, user):
        self.start_road = False
        self.last_status_change = None
        self.fare_total = 0
        self.in_movement = False
        self.start_time = None
        self.end_time = None
        self.user = user[0]
        logging.info(f"Taximetro inicializado para el usuario {self.user}")

#se define la funcion calculate fare, esta funcion calcula la tarifa teniendo en cuenta 
#el tiempo segun demanda y el valor de tarifa base

    def calculate_fare(self):
        now = time.time()
        if self.last_status_change is not None:
            time_elapsed = now - self.last_status_change
            fare = calculate_peak_fare(self.in_movement)
            self.fare_total += round(time_elapsed * fare, 2)
        self.last_status_change = now

#se define la funcion start, inicia el programa teniendo en cuenta que el taxi esta en movimiento y el tiempo 
    def start(self):
        self.start_road = True
        self.last_status_change = time.time()
        self.start_time = datetime.now()
        logging.info("Comenzar la carrera.")
        print("Comenzar la carrera.")

#se define la funcion stop, que detiene el taximetro teniendo en cuenta que el taxi esta parado, cambia el calculo de tarifa en base
#a la tarifa en pausa y el tiempo, muestra el mensaje del print
    def stop(self):
        if self.in_movement:
            self.calculate_fare()
            self.in_movement = False
            logging.info("El taxi se ha detenido.")
            print("El taxi se ha detenido.")
        else:
            print("Inicie el movimiento")

#se define la funcion continue_road, permite continuar la carrera despues de haberse detenido el taxi, vuelve a calcualar
#la tarifa en base al cambio de instruccion
    def continue_road(self):
        if self.start_road and self.in_movement == False:
            self.calculate_fare()
            self.in_movement = True
            logging.info("El taxi está en movimiento.")
            print("El taxi está en movimiento.")
        else:
            print("El taxi ya esta en movimiento.")

#se define la funcion finalizar, define la tarifa total de la carrera, se imprime el valor en euros, se guarda el historial 
#en una base de datos SQLite, en un texto plano.
    def finish_road(self):
        if self.start_road:
            self.calculate_fare()
            self.start_road = False
            self.end_time = datetime.now()
            logging.info(f"La carrera ha terminado. El total a cobrar es: {self.fare_total:.2f} euros.")
            print(f"La carrera ha terminado. El total a cobrar es: {self.fare_total:.2f} euros.")
            self.save_ride_history()
            db = Database()
            db.add_trip_database(self.start_time, self.end_time, round(self.fare_total,2), self.user)
            return self.fare_total
        else:
            print("La carrera no ha sido iniciada")

#se define la funcion para guardar el historial de la carrera en un archivo txt y mostrando caracteres unicode utf8
    def save_ride_history(self):
        with open('rides_history.txt', mode='a', encoding='utf-8') as file:
            file.write(f"Fecha de inicio: {self.start_time}\n")
            file.write(f"Fecha de fin: {self.end_time}\n")
            file.write(f"Total a cobrar: €{self.fare_total:.2f}\n")
            file.write("=======================================\n")
        logging.info("Historial de viaje guardado.")

#se define la funcion para ver el historual, abriendo el archivo txt creado en la funcion anterior, se exceptua errores
#para evitar que no funcione el programa
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

#se define la funcion para ver y escribir el historial en una base de datos, se importo la funcion Database del archivo Ds_psw
    def history_db(self):
        db = Database()
        db.show_history(self.user)
        logging.info("Historial de la base de datos visualizado.")

#se define la funcion clear, en donde el taxi no esta en movimiento, y los estados de los atributos vuelven a reiniciarse,
#el programa queda a la espera de nuevas instruccione
    def clear(self):
        self.start_road = False
        self.last_status_change = None
        self.fare_total = 0
        self.in_movement = False
        self.start_time = None
        self.end_time = None
        logging.info("Datos del taxímetro reiniciados.")

