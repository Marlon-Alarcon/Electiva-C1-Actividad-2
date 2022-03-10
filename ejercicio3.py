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

     #print(ListaConElementos)

     for i in range(6):
         print(ListaConElementos[i])


def main():
    listas()


if __name__=="__main__":
    main() 