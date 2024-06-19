from model import Taximetro

#Función main():
#Crea una instancia de la clase Taximetro.
#Imprime las instrucciones para el usuario.
#Entra en un bucle infinito para leer comandos del usuario y llamar a los métodos correspondientes del taxímetro.
def main():
    taximetro = Taximetro()

    print("Bienvenido al Taxímetro Digital!")
    print("Estos son los comandos disponibles: empezar, parar, continuar, finalizar; con ellos puede usar el programa.")

    while True:
        comando = input("Ingrese un comando: ")

        if comando == "empezar":
            taximetro.start()
        elif comando == "parar":
            taximetro.stop()
        elif comando == "continuar":
            taximetro.continue_road()
        elif comando == "finalizar":
            taximetro.finish_road()
        else:
            print("Comando inválido. Intente de nuevo.")


if __name__ == "__main__":
    main()