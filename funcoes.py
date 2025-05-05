import random
def rolar_dados(n):
    lista = []
    for numero in range(n):
        numero = random.randint(1,6)
        lista.append(numero)
    return lista

def guardar_dado (rodados, guardados, indice):
    guardados.append(rodados[indice])
    del rodados[indice]
    return [rodados, guardados]

def remover_dado(drolados,destoques,dremover):
    drolados.append(destoques[dremover])
    del destoques[dremover]
    return [drolados, destoques]
