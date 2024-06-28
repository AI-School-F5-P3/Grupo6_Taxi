from model import Taximetro
import time
from logger import log_info, log_warning, log_error


#se llama a la funcion main con el argumento user
def main(user):
    taximetro = Taximetro(user)


#se muestra la bienvenida
#se explican los comandos de uso del CLI
    log_info("Bienvenido al Taxímetro Digital! Programa iniciado.")
    print("Bienvenido al Taxímetro Digital!")
    print('''Estos son los comandos disponibles: 
          - "E" para empezar 
          - "P" para parar 
          - "C" para continuar
          - "F" para finalizar
          - "H" para visualizar el Historial
          - "X" para salir
            con ellos puede usar el programa.\n''')

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
            print('''Estos son los comandos disponibles: 
                - "E" para empezar 
                - "P" para parar 
                - "C" para continuar
                - "F" para finalizar
                - "H" para visualizar el Historial
                - "X" para salir
                    con ellos puede usar el programa.\n''')
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