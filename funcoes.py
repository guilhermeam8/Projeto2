import random
def rolar_dados(n):
    lista = []
    for numero in range(n):
        numero = random.randint(1,6)
        lista.append(numero)
    return lista
