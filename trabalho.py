import math

def sucessor(tabuleiro) -> list:
	
    estados = []
    
    countX = 0
    countO = 0	

    vez = None

    # descobre a vez
    for i in range(len(tabuleiro)):
        if(tabuleiro[i] == 'X'):
            countX += 1
        else:
            countO += 1

    # atribui a vez  
    if(countX < countO):
        vez = 'X'
    elif(countX > countO):
        vez = 'O'

    #print(tabuleiro)
    for i in range(9):        
        if (tabuleiro[i] != '-'):
            continue
        aux = tabuleiro[:]
        aux[i] = vez
        estados.append(aux)
    
    return estados

def sucessor2(tabuleiro) -> list:
	
    estados = []
    #print(tabuleiro)
    
    for i in range(9): 
        if (tabuleiro[i] != '-'):
            continue
        tabAux = tabuleiro[:]
        # mover pra cima
        if i - 3 >= 0:
            aux = tabAux[i-3]
            tabAux[i-3] = tabAux[i]
            tabAux[i] = aux
            estados.append(tabAux)

        tabAux = tabuleiro[:]

        # mover pra direita
        if math.trunc(i/3) == math.trunc((i+1)/3) and i+1 <= 9:
            aux = tabAux[i+1]
            tabAux[i+1] = tabAux[i]
            tabAux[i] = aux
            estados.append(tabAux)
        
        tabAux = tabuleiro[:]

        # mover para baixo
        if i + 3 <= 9:
            aux = tabAux[i+3]
            tabAux[i+3] = tabAux[i]
            tabAux[i] = aux
            estados.append(tabAux)

        tabAux = tabuleiro[:]

        # mover para esquerda
        if math.trunc(i/3) == math.trunc((i-1)/3) and i-1 >= 0:
            aux = tabAux[i-1]
            tabAux[i-1] = tabAux[i]
            tabAux[i] = aux
            estados.append(tabAux)
        
    #print(estados)
    return estados

def main():

    # abre/ler arquivo
    arquivo_velha = open('jogo_da_velha.txt', 'r')
    arquivo_puzzle = open('n_puzzle.txt', 'r')
    # ler/remove a primeira linha
    
  
    # le tudo com string   
    unica_string = arquivo_velha.read()

    linhas = unica_string.split('\n')# separa linhas em lista   

    #print(linhas)
    
    linha1 = linhas[0].split(' ') # transforma a em lista
    linha2 = linhas[1].split(' ')
    linha3 = linhas[2].split(' ')

    linhas = [linha1, linha2, linha3]

    tabuleiro = linha1 + linha2 + linha3

    fila = [tabuleiro]

    # busca largura

    nivel = 0
    while True:
        atual = fila.pop(0)
        print('tabuleiro {} {}'.format(nivel, atual))
        sucessores = sucessor(atual)        
        if len(sucessores) == 0:
            break
        fila += sucessores
        nivel +=1 

    print('-')

    unica_string = arquivo_puzzle.read()

    linhas = unica_string.split('\n')# separa linhas em lista   

    #print(linhas)
    
    linha1 = linhas[0].split(' ') # transforma a em lista
    linha2 = linhas[1].split(' ')
    linha3 = linhas[2].split(' ')

    linhas = [linha1, linha2, linha3]

    tabuleiro = linha1 + linha2 + linha3
    
    #Buca por profundidade
    P = 3
    n = 0
    empilha = True
    pilha = [tabuleiro]
    
    while True:
        if(len(pilha) == 0):
            break
        atual = pilha.pop(0)
        print(atual)
        if n < P:
            sucessores = sucessor2(atual)    
            if len(sucessores) == 0:
                break
            pilha = sucessores + pilha
            n+=1
        
    arquivo_velha.close()  
    arquivo_puzzle.close()   
         
        
           

main()