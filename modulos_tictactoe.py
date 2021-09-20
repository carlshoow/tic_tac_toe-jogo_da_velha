def mostrar(mat):
    print('~~' * 20)
    print(f'{"TIC TAC TOE":^40}')
    print('~~' * 20)

    for c in range(3):
        print()
        for j in range(3):
            if j == 0 or j == 1:
                print(f'{mat[c][j]:^10}|', end='')
                continue
            print(f'{mat[c][j]:^10}', end='')

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
        for j in range(0, 3):
            if escolha == mat[c][j]:
                if mat[c][j] != 'X' or mat[c][j] != 'Ø':
                    mat[c][j] = XouO
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
    for c in mat:
        if c.count('X') == 3 or c.count('Ø') == 3:
            return True
    # Verificar as verticais
    for l in range(3):
        if mat[0][l] == mat[1][l] and mat[0][l] == mat[2][l]:
            return True

    # Verifica diagonal 1
    if mat[0][0] == mat[1][1] and mat[0][0] == mat[2][2]:
        return True
    # Verifica diagonal 2
    if mat[0][2] == mat[1][1] and mat[0][2] == mat[2][0]:
        return True
