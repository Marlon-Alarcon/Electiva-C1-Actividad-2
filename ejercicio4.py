from api.library import *
import msvcrt

def Forma1():

    persona = {
        "nombre" : "Marlon",
        "apellido" : "Alarcon",
        "edad" : "22"
    }
    print("")
    print("Sin Interpolacion")
    print(persona["nombre"]+" " + persona["apellido"]+" "+persona["edad"])
    print("Con Interpolacion")
    print("")
    print(f"{persona['nombre']} {persona['apellido']} {persona['edad']}")
    print("")
    print("---> Presione una tecla para continuar")
    

def menu():
    men = 0
    while men != 3:
        print("")
        print("   MENÚ   ")
        print("1. Forma 1")
        print("2. Forma 2")
        print("3. Salir")
        print("")
        men = int(input("Ingrese una opcion por favor "))

        if men == 1:
            Forma1()
            msvcrt.getch()
        
        elif men == 2:
            print("")
            print("hola opcion 2")
            msvcrt.getch()

        elif men == 3:
            print("")
            print("-----   Has salido   -----")
            print("***** Muchas Gracias *****")
        
        else:
            print("")
            print(" -----  Opcion no valida  -----")
            print(" ----- Intente Nuevamente -----")


if __name__ == "__main__":
    menu()