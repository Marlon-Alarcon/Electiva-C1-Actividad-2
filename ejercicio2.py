# Andrea Camargo

from api.library import *

def main():
    SALARIO_MIN = 1000000
    SUB_ALIM = 120000
    SUB_TRANS = 80000
    BONO = 50000
    nombre = input("Digite el nombre: ")
    salario = int(input("Digite el salario mensual: "))
    diastrabajados = int(input("Digite los dias trabajados: "))
    sueldopagar = calcularsueldo(salario, diastrabajados)

    