import funcoes as f

cartela = {'regra_simples': {i: -1 for i in range(1, 7)}, 'regra_avancada': {k: -1 for k in ['sem_combinacao', 'quadra', 'full_house', 'sequencia_baixa', 'sequencia_alta', 'cinco_iguais']}}
f.imprime_cartela(cartela)
r = 0  
while (-1 in cartela['regra_simples'].values() or -1 in cartela['regra_avancada'].values()) and r != 12:
    dr = f.rolar_dados(5)  
    dg = []  
    rr = 0  
    ra = True  
    r += 1
    inv = False  
    
    while ra:
        if not inv:
            print(f"Dados rolados: {dr}")
            print(f"Dados guardados: {dg}")
            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")

        op = input()  
        inv = False

        if op == '1':
            print(f"Digite o índice do dado a ser guardado (0 a 4):")
            idx = int(input())
            dr, dg = f.guardar_dado(dr, dg, idx)

        elif op == '2':
            print(f"Digite o índice do dado a ser removido (0 a 4):")
            idx = int(input())
            dr, dg = f.remover_dado(dr, dg, idx)

        elif op == '3':
            if rr < 2:
                dr = f.rolar_dados(len(dr))
                rr += 1
            else:
                print("Você já usou todas as rerrolagens.")

        elif op == '4':
            f.imprime_cartela(cartela)

        elif op == '0':
            print("Digite a combinação desejada:")
            while True:
                resp = input()  
                if resp.isdigit():
                    resp_int = int(resp)
                else:
                    resp_int = None
                while resp_int not in cartela['regra_simples'] and resp not in cartela['regra_avancada']:
                    print("Combinação inválida. Tente novamente.")
                    resp = input() 
                    if resp.isdigit():
                        resp_int = int(resp)
                    else:
                        resp_int = None
                if resp_int in cartela['regra_simples']:
                    if cartela['regra_simples'][resp_int] == -1:
                        f.faz_jogada(dr + dg, resp, cartela)
                        break
                    else:
                        print("Essa combinação já foi utilizada.")
                elif resp in cartela['regra_avancada']:
                    if cartela['regra_avancada'][resp] == -1:
                        f.faz_jogada(dr + dg, resp, cartela)
                        break
                    else:
                        print("Essa combinação já foi utilizada.")
            break 

        else:
            print("Opção inválida. Tente novamente.")
            inv = True  

ts = sum(cartela['regra_simples'].values())  
ta = sum(cartela['regra_avancada'].values())  
total = ts + ta + (35 if ts >= 63 else 0)

f.imprime_cartela(cartela)
print(f"Pontuação total: {total}")


