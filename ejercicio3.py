# Andres Castellon

print("Hola mundo")

# ***********************************
#           Manejo de listas
# ***********************************

"""
*************************************************
                Manejo de listas
*************************************************

"""

def  listas():
     lista1 = []
     lista2 = list()

     ListaConElementos = [30, 2000000, "Andres Castellon", "Personal de tienda", True, ["Bachiller", "Pregrado", "Tecnico", 20]]
     print("")
     print(ListaConElementos)

      # Utilizando ciclo for
     print("")
     print("Mostrando elementos con ciclo for :)")

     for i in range(len(ListaConElementos)):
         print(ListaConElementos[i])


def main():
    listas()


if __name__=="__main__":
    main()          