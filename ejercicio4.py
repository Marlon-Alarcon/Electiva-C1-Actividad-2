from api.library import *

def main():

    persona = {
        "nombre" : "Marlon",
        "apellido" : "Alarcon",
        "edad" : "22"
    }

    print(persona["nombre"]+" " + persona["apellido"]+" "+persona["edad"])


if __name__ == "__main__":
    main()