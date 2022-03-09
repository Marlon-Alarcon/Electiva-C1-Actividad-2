# Marlon Alarcon
from api.library import *
import msvcrt

def Forma1():

    persona = {
        "nombre" : "Marlon",
        "apellido" : "Alarcon",
        "edad" : "22"
    }
    print("")
    print(" Sin Interpolacion")
    print(persona["nombre"]+" " + persona["apellido"]+" "+persona["edad"])
    print(" Con Interpolacion")
    print("")
    print(f"{persona['nombre']} {persona['apellido']} {persona['edad']}")
    print("")
    print("---> Presione una tecla para continuar")

def Forma2():
    persona = {
        "datos_personales":{
        "nombre": "Marlon",
        "apellidos": "Alarcon",
        "edad": 22
        },

        "salarial": {
            "salario": 2000000,
            "sub-transporte": 50000,
            "sub-alimentacion": 60000
        }
    }
    print(persona["salarial"])
    #print (f"Salario: {persona ['salarial']['salario']}")
    print(f"Nombre: {persona ['datos_personales']['nombre']} {persona ['datos_personales']['apellidos']}")
    print(f"Edad: {persona['datos_personales']['edad']}")
    print("")
    print("---> Presione una tecla para continuar")
    

def menu():
    men = 0
    while men != 3:
        print("")
        print("  ----  MENÚ  -----  ")
        print("")
        print("1. Un objeto")
        print("2. Dos objetos en uno")
        print("3. Salir")
        print("")
        men = int(input("Ingrese una opcion por favor "))

        if men == 1:
            Forma1()
            msvcrt.getch()
        
        elif men == 2:
            print("")
            Forma2()
            msvcrt.getch()

        elif men == 3:
            print("")
            print("-----   Has salido   -----")
            print("***** Muchas Gracias *****")
        
        else:
            print("")
            print(" -----  Opcion no valida  -----")
            print(" ----- Intente Nuevamente -----")
            print("")
            print("-- Presione una tecla para continuar")
            msvcrt.getch()


if __name__ == "__main__":
    menu()