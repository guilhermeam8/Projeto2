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
def calcula_pontos_sequencia_baixa(faces):
    sequencias = [[1, 2, 3, 4],[2, 3, 4, 5],[3, 4, 5, 6]]
    for sequencia in sequencias:
        contador = 0
        for numero in sequencia:
            if numero in faces:
                contador += 1
        if contador == 4:
            return 15
    return 0
def calcula_pontos_sequencia_alta(faces):
    sequencias = [[1,2,3,4,5],[2,3,4,5,6]]
    for sequencia in sequencias:
        contador = 0
        for numero in sequencia:
            if numero in faces:
                contador+=1
        if contador == 5:
            return 30
    return 0
def calcula_pontos_full_house(faces):
    for i in range(len(faces)):
        valorrr = faces[i]
        contadorrr = 0
        for n in range(len(faces)):
            if faces[n] == valorrr:
                contadorrr +=1
        if contadorrr == 3:
            for m in range(len(faces)):
                valorr = faces[m]
                if valorr != valorrr:
                    contadorr = 0
                    for k in range(len(faces)):
                        if faces[k] == valorr:
                            contadorr +=1
                    if contadorr == 2:
                        soma = 0
                        for j in range(len(faces)):
                            soma+=faces[j]
                        return soma
    return 0
def calcula_pontos_quadra(faces):
    for i in range(len(faces)):
        numero = faces[i]
        contador = 0
        for k in range(len(faces)):
            if faces[k] == numero:
                contador+=1
        if contador >= 4:
            soma = 0
            for p in range(len(faces)):
                soma += faces[p]
            return soma
    return 0
def calcula_pontos_quina(faces):
    for i in range(len(faces)):
        numero = faces[i]
        if not numero in faces[:i]:
            contador = 0
            for k in range(len(faces)):
                if faces[k] == numero:
                    contador += 1
            if contador >= 5:
                return 50
    return 0
def calcula_pontos_regra_avancada (faces):
    return {
        'cinco_iguais': calcula_pontos_quina(faces),
        'full_house': calcula_pontos_full_house(faces),
        'quadra': calcula_pontos_quadra(faces),
        'sem_combinacao': calcula_pontos_soma(faces),
        'sequencia_alta': calcula_pontos_sequencia_alta(faces),
        'sequencia_baixa': calcula_pontos_sequencia_baixa(faces)
    }
def faz_jogada(dados, tipo, tabela):
    if tipo in ['1', '2', '3', '4', '5', '6']: 
        i = int(tipo)
        pts = calcula_pontos_regra_simples(dados)[i]
        tabela['regra_simples'][i] = pts 
    elif tipo in tabela['regra_avancada']:
        pts = calcula_pontos_regra_avancada(dados)[tipo]
        tabela['regra_avancada'][tipo] = pts 
    return tabela