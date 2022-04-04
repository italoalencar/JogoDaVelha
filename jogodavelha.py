import os

# Criando o Tabuleiro
def criar_tab():
    tab = []
    for i in range(3):
        lista = 3 * [' ']
        tab.append(lista)
    return tab    

# Mostrar o Tabuleiro
def printar_tab(tab):
    print('   1\t   2\t   3')      
    print('A    %s\t|  %s  |\t  %s' % (tab[0][0],tab[0][1],tab[0][2]))
    print(' ',19*'-')
    print('B    %s\t|  %s  |\t  %s' % (tab[1][0],tab[1][1],tab[1][2]))
    print(' ',19*'-')
    print('C    %s\t|  %s  |\t  %s' % (tab[2][0],tab[2][1],tab[2][2]))
    print("")

# Entrada
def entra(jogador):
    while True:
        entrada = input('Jogador %s, digite sua jogada na forma (linhaXcoluna): ' % jogador).upper()

        excluir = "X, ()"   # Caracteres que serao ignorados
        for i in excluir:
            entrada = entrada.replace(i,"")

        jogada = []         # Jogada sera uma lista onde cada posiçao assumira um caractere da entrada
        for i in entrada:     
            jogada.append(i)

        if len(jogada) == 2:            # Verifica se a lista esta formatada. Caso nao, sera pedido outra entrada
            if jogada[0] == 'A' or jogada[0] == 'B' or jogada[0] == 'C':
                if jogada[1] == '1' or jogada[1] == '2' or jogada[1] == '3':
                    break
        print("Jogada inválida, tente novamente.")     
    return jogada

# Jogada X
def jogadaX(tab):
    jogada = entra('X')
    print("")
    
    # Tratando a posicao da linha onde será feito a jogada
    if jogada[0] == 'A':
        jogada[0] = 0
    elif jogada[0] == 'B':
        jogada[0] = 1
    else:
        jogada[0] = 2    

    jogada[1] = int(jogada[1]) - 1 # Tratando a posicao da coluna onde será feito a jogada
    preencher_x(tab,jogada)

# Função do Jogador X
def preencher_x(tab,jogada):
    if tab[jogada[0]][jogada[1]] == ' ':
        tab[jogada[0]][jogada[1]] = 'X'
        os.system('cls')
        printar_tab(tab)
    else:
        print('*Espaço marcado, Tente outra jogada')
        print("")
        jogadaX(tab)

# Verifica se o Jogador X ganhou
def verificax(tab):
    for i in range(3):
        if tab[i][0]+tab[i][1]+tab[i][2] == 'XXX':
            print('Jogador X venceu!')
            return True                   
        elif tab[0][i]+tab[1][i]+tab[2][i] == 'XXX':
            print('Jogador X venceu!')
            return True
    if tab[0][0]+tab[1][1]+tab[2][2] == 'XXX':
        print('Jogador X venceu!') 
        return True
    elif tab[0][2]+tab[1][1]+tab[2][0] == 'XXX':
        print('Jogador X venceu!')
        return True
    else:
        return False

# Jogada O
def jogadaO(tab):
    jogada = entra('O')
    print("")

    # Tratando a posicao da linha onde será feito a jogada
    if jogada[0] == 'A':
        jogada[0] = 0
    elif jogada[0] == 'B':
        jogada[0] = 1
    else:
        jogada[0] = 2    

    jogada[1] = int(jogada[1]) - 1 # Tratando a posicao da coluna onde será feito a jogada
    preencher_O(tab,jogada)

# Função do Jogador O
def preencher_O(tab,jogada):
    if tab[jogada[0]][jogada[1]] == ' ':
        tab[jogada[0]][jogada[1]] = 'O'
        os.system('cls')
        printar_tab(tab)
    else:
        print('*Espaço marcado, Tente outra jogada')
        print("")
        jogadaO(tab)

# Verifica se o Jogador O ganhou
def verificao(tab):
    for i in range(3):
        if tab[i][0]+tab[i][1]+tab[i][2] == 'OOO':
            print('Jogador O venceu!')
            return True
        elif tab[0][i]+tab[1][i]+tab[2][i] == 'OOO':
            print('Jogador O venceu!')
            return True
    if tab[0][0]+tab[1][1]+tab[2][2] == 'OOO':
        print('Jogador O venceu!')
        return True
    elif tab[0][2]+tab[1][1]+tab[2][0] == 'OOO':
        print('Jogador O venceu!')
        return True
    else:
        return False

# Execução
os.system('cls')
maisum = 1
while maisum == 1:
    teste = False
    vez = 1
    jogadas = 0

    tab = criar_tab()
    printar_tab(tab)
    while teste == False and jogadas < 9:
        if vez == 1:
            jogadaX(tab)
            teste = verificax(tab)
            vez = 0
            jogadas += 1
        elif vez == 0:
            jogadaO(tab)
            teste = verificao(tab)
            vez = 1
            jogadas += 1       
    if teste == False and jogadas == 9:
        print("")
        print('Deu empate!')

    while True:
        maisum = input("Voce quer jogar novamente? 1-sim 0-nao\n")
        if maisum == '1' or maisum == '0':
            maisum = int(maisum)
            os.system('cls')
            break
        else:
            print("Voce digitou um comando invalido. Tente Novamente.")
print("Até a próxima!") 