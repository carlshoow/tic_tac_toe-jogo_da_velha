import modulos_tictactoe as modulo
while True:
    tictactoe = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    jogadas = 0
    x_ou_o = 'X'
    while True:
        modulo.mostrar(tictactoe)
        try:
            escolha = int(input(f'(000 para EXIT) Escolha um numero para marcar [{x_ou_o}]: '))
        except:
            continue
        if escolha == 000:
            break
        #Inicio do jogo
        if(modulo.jogar(tictactoe, escolha, x_ou_o)):
            jogadas += 1

        else:
            print('\033[1:31mEscolha Invalida!\033[m')
            continue

        #Verifica o ganhador
        if jogadas > 4:
            ganhador = modulo.ganhador(tictactoe)
            if ganhador:
                break
            elif jogadas == 9:
                break

        #Troca de X para O e vice-versa
        x_ou_o = modulo.troca_XouO(x_ou_o)

    modulo.mostrar(tictactoe)
    if ganhador:
        print('O ganhador foi [{}]'.format(x_ou_o))

    if jogadas == 9 and  not ganhador:
        print('Deu velha!')
    print('='*20)

    dnv = str(input('Quer jogar novamente? [S/N] ')).strip().upper()[0]
    if dnv == 'N':
        break