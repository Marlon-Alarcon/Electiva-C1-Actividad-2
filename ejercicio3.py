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

     # Utilizando ciclo for

     print("Mostrando elementos con ciclo for :)")

     for i in range(len(ListaConElementos)):
         print(ListaConElementos[i])

     # Utilizando ciclo while

     print("")
     print("")
     print("")
     print("Mostrando elementos con ciclo while :)")

     j=0
     while j < len(ListaConElementos):
         print(ListaConElementos[j])
         #j = j + 1
         j+= 1

     print("")
     print("")
     print(ListaConElementos[5][3])
     
     print("")
     print("")
     print(ListaConElementos[-1][3])




def main():
    listas()


if __name__=="__main__":
    main() 