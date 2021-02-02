#!/usr/bin/env python3
#*******************************************************************************
# Funcao: atualizaTabela
#
# Parametros:
#   tabela: uma matriz com os dados da tabela do campeonato
#   jogo: string contendo as informações de um jogo no formato especificado no lab.
#
# Descrição:
#   Deve inserir as informações do parametro 'jogo' na tabela.
#   OBSERVAÇÃO: nesse momento não é necessário ordenar a tabela, apenas inserir as informações.
def atualizaTabela(tabela, jogo):
#  -- INSIRA SEU CÓDIGO AQUI -- #
#*******************************************************************************
#FUNCIONANDO
    jogo=jogo.split()
    time1, gols1, gols2, time2= jogo[0], int(jogo[1]), int(jogo[3]), jogo[4]
    for a in range(len(tabela)):
        if time1==tabela[a][0]:
            pos1=a
    for b in range(len(tabela)):
        if time2==tabela[b][0]:
            pos2=b
    if gols1>gols2:
        tabela[pos1][1]+=3
        tabela[pos1][2]+=1
    if gols1<gols2:
        tabela[pos2][1]+=3
        tabela[pos2][2]+=1
    if gols1==gols2:
        tabela[pos1][1]+=1
        tabela[pos2][1]+=1
    tabela[pos1][3]=tabela[pos1][3]+gols1-gols2
    tabela[pos1][4]=tabela[pos1][4]+gols1
    tabela[pos2][3]=tabela[pos2][3]+gols2-gols1
    tabela[pos2][4]=tabela[pos2][4]+gols2

#*******************************************************************************
# Funcao: comparaTimes
#
# Parametros:
#   time1: informações de um time
#   time2: informações de um time
#
# Descricão:
#   retorna 1, se o time1>time2, retorna -1, se time1<time2, e retorna 0, se time1=time2
#   Observe que time1>time2=true significa que o time1 deve estar em uma posição melhor do que o time2 na tabela.
def comparaTimes(time1, time2):
#  -- INSIRA SEU CÓDIGO AQUI -- #
#*******************************************************************************
    if time1>time2:
        return 1
    if time1<time2:
        return -1
    if time1==time2:
        return 0
#*******************************************************************************
# Funcao: ordenaTabela
#
# Parametros:
#   tabela: uma matriz com os dados da tabela do campeonato.
#
# Descricão:
#   Deve ordenar a tabela com campeonato de acordo com as especificaçoes do lab.
#
def ordenaTabela(tabela):
#  -- INSIRA SEU CÓDIGO AQUI -- #
#*******************************************************************************
    for i in range(len(tabela)-1):
        for j in range(i, len(tabela)):
            if comparaTimes(tabela[i][1], tabela[j][1]) == 0:
                if comparaTimes(tabela[i][2], tabela[j][2]) == 0:
                    if comparaTimes(tabela[i][3], tabela[j][3]) == 0:
                        if comparaTimes(tabela[i][4], tabela[j][4]) == -1:
                            tabela[i], tabela[j]=tabela[j], tabela[i]
                    elif comparaTimes(tabela[i][3], tabela[j][3]) == -1:
                        tabela[i], tabela[j]=tabela[j], tabela[i]
                elif comparaTimes(tabela[i][2], tabela[j][2]) == -1:
                    tabela[i], tabela[j]=tabela[j], tabela[i]
            elif comparaTimes(tabela[i][1], tabela[j][1]) == -1:
                tabela[i], tabela[j]=tabela[j], tabela[i]


#*******************************************************************************
# Funcao: imprimeTabela
#
# Parametros:
#   tabela: uma matriz com os dados da tabela do campeonato.
#
# Descrição:
#   Deve imprimir a tabela do campeonato de acordo com as especificações do lab.
def imprimeTabela(tabela):
#  -- INSIRA SEU CÓDIGO AQUI -- #
#*******************************************************************************
    for i in tabela:
        print(str(i[0])+", "+str(i[1])+", "+str(i[2])+", "+str(i[3])+", "+str(i[4]))
