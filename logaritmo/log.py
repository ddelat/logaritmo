import math


def calcular_logaritmo_neperiano(numero):
    if numero > 0:
        resultado=math.log(numero)
        print(f"El logaritmo neperiano de {numero} es: {resultado}")
    else:
        print("Error en el numero,", numero, "tiene que ser positivo")


# Ejemplo de uso
numero = 10
calcular_logaritmo_neperiano(numero)
numero2 = -1
calcular_logaritmo_neperiano(numero2)
