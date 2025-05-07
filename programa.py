import funcoes as f

cart = {
    'regra_simples': {n: -1 for n in range(1, 7)},
    'regra_avancada': {k: -1 for k in ['sem_combinacao', 'quadra', 'full_house', 'sequencia_baixa', 'sequencia_alta', 'cinco_iguais']}
}

f.imprime_cartela(cart)
rod = 0

while rod < 12 and (-1 in cart['regra_simples'].values() or -1 in cart['regra_avancada'].values()):
    rol = f.rolar_dados(5)
    guard = []
    rer = 0
    rod += 1
    seguir = True
    erro = ''

    while seguir:
        if not erro:
            print(f"Dados rolados: {rol}")
            print(f"Dados guardados: {guard}")
            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
        op = input()
        erro = ''

        if op == '1':
            print(f"Digite o índice do dado a ser guardado (0 a 4):")
            i = int(input())
            rol, guard = f.guardar_dado(rol, guard, i)

        elif op == '2':
            print(f"Digite o índice do dado a ser removido (0 a 4):")
            i = int(input())
            rol, guard = f.remover_dado(rol, guard, i)

        elif op == '3':
            if rer < 2:
                rol = f.rolar_dados(len(rol))
                rer += 1
            else:
                print("Você já usou todas as rerrolagens.")
        elif op == '4':
            f.imprime_cartela(cart)

        elif op == '0':
            print("Digite a combinação desejada:")
            cat = input()

            if cat.isdigit():
                catn = int(cat)
                if catn in cart['regra_simples'] and cart['regra_simples'][catn] == -1:
                    f.faz_jogada(rol + guard, cat, cart)
                    seguir = False
                else:
                    erro = 'X'
                    print("Inválido ou já usado.")
            elif cat in cart['regra_avancada']:
                if cart['regra_avancada'][cat] == -1:
                    f.faz_jogada(rol + guard, cat, cart)
                    seguir = False
                else:
                    erro = 'X'
                    print("Já usado.")
            else:
                erro = 'X'
                print("Categoria inválida.")
        else:
            erro = 'X'
            print("Opção inválida.")

p_sim = sum(cart['regra_simples'].values())
p_av = sum(cart['regra_avancada'].values())
bns = 35 if p_sim >= 63 else 0
ttl = p_sim + p_av + bns

f.imprime_cartela(cart)
print(f"Total: {ttl}")
