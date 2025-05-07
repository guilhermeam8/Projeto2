import funcoes as f

cart = {
    'regra_simples': {i: -1 for i in range(1, 7)},
    'regra_avancada': {k: -1 for k in ['sem_combinacao', 'quadra', 'full_house', 'sequencia_baixa', 'sequencia_alta', 'cinco_iguais']}
}

f.imprime_cartela(cart)
rod = 0

while (-1 in cart['regra_simples'].values() or -1 in cart['regra_avancada'].values()) and rod != 12:
    rol = f.rolar_dados(5)
    guard = []
    rer = 0
    jogando = True
    rod += 1
    inval = False

    while jogando:
        if not inval:
            print(f"Dados rolados: {rol}")
            print(f"Dados guardados: {guard}")
            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
        op = input()
        inval = False

        if op == '1':
            print(f"Digite o índice do dado a ser guardado (0 a {len(rol)-1}):")
            idx = int(input())
            if 0 <= idx < len(rol):
                rol, guard = f.guardar_dado(rol, guard, idx)
            else:
                print("Índice inválido.")

        elif op == '2':
            print(f"Digite o índice do dado a ser removido (0 a {len(guard)-1}):")
            idx = int(input())
            if 0 <= idx < len(guard):
                rol, guard = f.remover_dado(rol, guard, idx)
            else:
                print("Índice inválido.")

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
            while True:
                cat = input()
                catn = int(cat) if cat.isdigit() else None

                while catn not in cart['regra_simples'] and cat not in cart['regra_avancada']:
                    print("Combinação inválida. Tente novamente.")
                    cat = input()
                    catn = int(cat) if cat.isdigit() else None

                if catn in cart['regra_simples']:
                    if cart['regra_simples'][catn] == -1:
                        f.faz_jogada(rol + guard, cat, cart)
                        break
                    else:
                        print("Essa combinação já foi usada.")
                elif cat in cart['regra_avancada']:
                    if cart['regra_avancada'][cat] == -1:
                        f.faz_jogada(rol + guard, cat, cart)
                        break
                    else:
                        print("Essa combinação já foi usada.")
            break

        else:
            print("Opção inválida. Tente novamente.")
            inval = True

pts_sim = sum(cart['regra_simples'].values())
pts_av = sum(cart['regra_avancada'].values())
bonus = 35 if pts_sim >= 63 else 0
total = pts_sim + pts_av + bonus

f.imprime_cartela(cart)
print(f"Pontuação total: {total}")
