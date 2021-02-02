#!/usr/bin/env python3

# Laboratorio 12 - Tetris
# Nome: Marcos Diaz
# RA: 221525

ALTURA_TABULEIRO = 10
LARGURA_TABULEIRO = 10

# Funcao: atualiza_posicao
#
# Parametros:
#      l: largura do bloco que ira cair
#      a: altura do bloco que ira cair
#      x: posicao horizontal inicial do bloco que ira cair
#   desl: deslocamento horizontal a ser aplicado ao bloco (positivo para direita, negativo para a esquerda)
#    rot: 1 se deve rotacionar o bloco, 0 caso contrario
#
# Retorno:
#   Nova largura, altura e posicao horizontal.
#
def atualiza_posicao(l, a, x, desl, rot):
    # Implementar a funcao e trocar o valor de retorno
    #rotacionar
    pos=0
    if rot == 1:
        largura=a
        altura=l
    else:
        largura=l
        altura=a
    #computar x
    if desl>=0:
        if x+largura+desl <=10:
            pos=x+desl
        else:
            pos=10-largura
    elif desl<0:
        if x+desl>=0:
            pos=x+desl
        else:
            pos=0
    #retornar
    return largura, altura, pos

# Funcao: encontra_y
#
# Parametros:
#    mat: matriz representando o tabuleiro
#      l: largura do bloco que ira cair
#      x: posicao horizontal do bloco que ira cair
#
# Retorno:
#   altura final y do canto inferior esquerdo do bloco apos
#   este descer o maximo possivel
#
def encontra_y(mat, l, x):
    # Implementar a funcao e trocar o valor de retorno
    yf=0
    for i in range(10):
        if 1 in mat[i][x:x+l]:
            yf= i+1
    return yf

# Funcoes: posicao_final_valida
#
# Parametros:
#      a: altura do bloco que caiu
#      y: altura final do bloco que caiu
#
# Retorno:
#   1 se o bloco naquela posicao estiver contido dentro do tabuleiro, ou 0 caso contrario.
#
def posicao_final_valida(a, y):
    # Implementar a funcao e trocar o valor de retorno
    if y+a<=10:
        return 1
    else:
        return 0

# Funcoes: posiciona_bloco
#
# Parametros:
#    mat: matriz do tabuleiro
#      l: largura do novo bloco
#      a: altura do novo bloco
#      x: posicao horizontal do novo bloco
#      y: altura final do novo bloco
#
#      Deve preencher com 1s as novas posicoes ocupadas pelo bloco que caiu
# Retorno:
#   NULL
#
def posiciona_bloco(mat, l, a, x, y):
    # Implementar a funcao
    for i in range(y, y+a):
        for j in range(x, x+l):
             mat[i][j]=1


# Funcoes: atualiza_matriz
#
#    mat: matriz do tabuleiro
#
#         Deve remover as linhas totalmente preenchidas do tabuleiro copiando
#         linhas posicionadas acima.
# Retorno:
#   retorna o numero de linhas totalmente preenchidas que foram removidas apos
#   a atualizacao do tabuleiro.
#
def atualiza_matriz(mat):
    # Implementar a funcao e trocar o valor de retorno
    p=0
    preenchida=[1 for i in range(10)]
    ref=[i[:] for i in mat]
    """
    if preenchida in ref:
        print("rodou if!")
        print(mat[0] is preenchida)
        while preenchida in ref:
            mat.remove(preenchida)
            mat.append([0 for z in range(10)])
            p=p+1
    """
    for i in range(10):
        if ref[9-i]==preenchida:
            #o indexerror esta aqui!
            newlast=[0 for z in range(10)]
            mat.pop(9-i)
            mat.append(newlast)
            p=p+1
    return p
