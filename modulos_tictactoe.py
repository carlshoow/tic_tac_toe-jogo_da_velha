def mostrar(mat):
    print('~~' * 20)
    print(f'{"TIC TAC TOE":^40}')
    print('~~' * 20)

    for c in range(3):
        print()
        for l in range(3):
            if l == 0 or l == 1:
                print(f'{mat[c][l]:^10}|', end='')
                continue
            print(f'{mat[c][l]:^10}', end='')

        print()
        if c != 2:
            print('--------------------------------', end='')
    print('')


def troca_XouO(XouO):
    # Se for X vira O
    if XouO == 'X':
        XouO = 'Ø'
        return XouO
    # Se for O vira X
    elif XouO == 'Ø':
        XouO = 'X'
        return XouO


def jogar(mat, escolha, XouO):
    '''
    Substitui os numeros pelas escolhas

    :param mat: Passa uma matriz como referencia
    :param escolha: Escolha do jogador 1-9
    :param XouO: Marca X ou O dependendo da função troca_XouO
    :return: True se a escolha for valida
    '''
    ok = False
    for c in range(0, 3):
        for l in range(0, 3):
            if escolha == mat[c][l]:
                if mat[c][l] != 'X' or mat[c][l] != 'Ø':
                    mat[c][l] = XouO
                    ok = True
                    return ok
                else:
                    return ok


def ganhador(mat):
    '''

    :param mat:Passa a matriz como referencia
    :return: retorna True quando existir algum ganhador
    '''

    # Verificar as horizontais
    for l in mat:
        if l.count('X') == 3 or l.count('Ø') == 3:
            return True
    # Verificar as verticais
    for c in range(3):
        if mat[0][c] == mat[1][c] and mat[0][c] == mat[2][c]:
            return True

    # Verifica diagonal 1
    if mat[0][0] == mat[1][1] and mat[0][0] == mat[2][2]:
        return True
    # Verifica diagonal 2
    if mat[0][2] == mat[1][1] and mat[0][2] == mat[2][0]:
        return True
