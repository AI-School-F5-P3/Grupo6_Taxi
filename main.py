from model import Taximetro
import time
from logger import log_info, log_warning, log_error

def show_menu(taximetro):
    print("\n---------------- Menú ------------------")
    print(f"\nTarifa movimiento: {taximetro.fare_movement}" \
		f"\nTarifa parado: {taximetro.fare_stop}\n")
    print('''Estos son los comandos disponibles: 
                - "E" para empezar 
                - "P" para parar 
                - "C" para continuar
                - "F" para finalizar
                - "H" para visualizar el Historial
                - "X" para salir\n''')

#se llama a la funcion main con el argumento user
def main(user):
    taximetro = Taximetro(user)

#se muestra la bienvenida
#se explican los comandos de uso del CLI
    log_info("Bienvenido al Taxímetro Digital! Programa iniciado.")
    print("\n\tBienvenido al Taxímetro Digital!")
    show_menu(taximetro)

#se inicia un bucle while con las condicionales para cada comando
    while True:
        comando = input("Ingrese un comando: ").upper()
        if comando == "E":
            taximetro.start()
            log_info(f"Comando {comando}: Taxímetro iniciado.")
        elif comando == "P":
            taximetro.stop()
            log_info(f"Comando {comando}: Taxímetro detenido.")
        elif comando == "C":
            taximetro.continue_road()
            log_info(f"Comando {comando}: Taxímetro continuado.")
        elif comando == "F":
            taximetro.finish_road()
            taximetro.clear()
            log_info(f"Comando {comando}: Taxímetro finalizado y reiniciado.")
            show_menu(taximetro)
        elif comando == "H":
            taximetro.history_db()
            log_info(f"Comando {comando}: Historial visualizado.")
        elif comando == "X":
            print("Gracias por usar nuestro taximetro.")
            log_info("Programa terminado por el usuario.")
            break
        else:
            print("Comando inválido. Intente de nuevo.")
            log_warning("Comando inválido ingresado.")


# Este bloque solo se ejecutará si este script es el punto de entrada principal
if __name__ == "__main__":
    user = "Usuario predeterminado"  # Asumiendo que se obtiene el nombre de usuario de alguna manera
    main(user)