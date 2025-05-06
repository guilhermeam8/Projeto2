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

def calcula_pontos_regra_simples(dados):
    contagem = {1:0,2:0,3:0,4:0,5:0,6:0}
    for face in dados:
        if 1<=face<= 6:
            contagem[face]+=1  
    resultado = {}
    for face in range(1,7):
        pontos = face*contagem[face]
        resultado[face] = pontos
    return resultado
def calcula_pontos_soma (lista):
    resposta = 0
    for numeros in lista:
        resposta += numeros
    return resposta
