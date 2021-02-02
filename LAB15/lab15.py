#!/usr/bin/env python3

# Funcao: pertence
#
# Parametros:
#   conj: vetor contendo o conjunto de entrada
#    num: elemento a ser verificado pertinencia
#
# Retorno:
#   True se num pertence a conj e False caso contrario
#
def pertence(conj, num):
    # Implementar a funcao e trocar o valor de retorno
    if num in conj:
        return True
    else:
        return False

# Funcao: contido
#
# Parametros:
#   conj1: vetor contendo um conjunto de entrada
#   conj2: vetor contendo um conjunto de entrada
#
# Retorno:
#   True se conj1 esta contido em conj2 e False caso contrario
#
def contido(conj1, conj2):
    # Implementar a funcao e trocar o valor de retorno
    for i in range(len(conj1)):
        if conj1[i] not in conj2:
            return False
    return True

# Funcoes: adicao e subtracao
#
# Parametros:
#   conj: vetor contendo o conjunto que tera incluso ou removido o elemento
#    num: elemento a ser adicionado ou removido
#
def adicao(conj, num):
    # Implementar a funcao
    if not pertence(conj, num):
        conj.append(num)

def subtracao(conj, num):
    # Implementar a funcao
    if pertence(conj, num):
        conj.remove(num)



# Funcoes: uniao, intersecao e diferenca
#
# Parametros:
#     conj1: vetor contendo o conjunto de entrada do primeiro operando
#     conj2: vetor contendo o conjunto de entrada do segundo operando
#
# Retorno:
#   Vetor contendo o conjunto de saida/resultado da operacao
#
def uniao(conj1, conj2):
    # Implementar a funcao e trocar o valor de retorno
    new=conj1+conj2
    for i in range(len(conj1)):
        if pertence(conj2, conj1[i]):
            new.remove(conj1[i])
    return new

def intersecao(conj1, conj2):
    # Implementar a funcao e trocar o valor de retorno
    new=[]
    for i in range(len(conj1)):
        if pertence(conj2, conj1[i]):
            new.append(conj1[i])
    return new

def diferenca(conj1, conj2):
    # Implementar a funcao e trocar o valor de retorno
    new=[]
    for i in range(len(conj1)):
        if not pertence(conj2, conj1[i]):
            new.append(conj1[i])
    return new

def uniao_disjunta(conj1, conj2):
    # Implementar a funcao e trocar o valor de retorno
    return diferenca(conj1, conj2)+diferenca(conj2, conj1)
