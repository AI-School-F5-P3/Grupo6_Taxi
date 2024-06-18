from model import Taximetro


def show_welcome():
	print("Bienvenida, instrucciones")


def main():
	taximetro = Taximetro()
	show_welcome()
	command = input("ingrese opcion: ")
	if command == "empezar":
		taximetro.finish_road()


main()