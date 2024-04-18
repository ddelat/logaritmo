import math


def calcular_logaritmo_neperiano(numero):
    if numero > 0:
        return math.log(numero)
    else:
        print('Error en el numero')


# Ejemplo de uso
numero = 10
resultado = calcular_logaritmo_neperiano(numero)
print(f"El logaritmo neperiano de {numero} es: {resultado}")
numero = -1
resultado = calcular_logaritmo_neperiano(numero)
