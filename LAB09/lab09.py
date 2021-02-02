#LAB09
#1. entrada - matriz (funcionando)
dias=int(input())
master=[[] for i in range(4)]
for i in range(4):
    for a in range(dias):
        master[i].append(float(input()))
#test1
print (master)
#2. gerar todas as operacoes possiveis (funcionando)
# para cada empresa-modelo: (c,v)
#2.2. reduzir possible para operacoes validas = FEITO
possible=[[] for i in range(4)]
for a in range(4):
    for c in range (dias+1):
        for v in range(dias+1):
            if v>c and v!=1 and c!=0:
                possible[a].append([c, v])

#test2
for a in range(4):
    print (possible[a])

#3. funcao recursiva do calculo dos lucros
#!# Lucro esta sendo uma lista infinita somente com o valor de lucro maximo !!!
lucros=[]
cmaxs=[0]
vmaxs=[0]
empresamaxs=[]
def lucromax():
    print ("cmaxs "+ str(cmaxs))
    print ("vmaxs "+ str(vmaxs))
    lucro=0
    ifrodou=0
    forrodou=0
    lastdcompramax=0
    lastdvendamax=0
    cmaxvmaxintermediaria=[]
    for b in range(len(cmaxs)):
        for c in range(len(vmaxs)):
            cmaxvmaxintermediaria.append([cmaxs[b], vmaxs[c]])
    print("cmaxvmaxintermediaria= "+ str(cmaxvmaxintermediaria))
    for i in range(4): #para cada empresa
        if i not in empresamaxs: #se ela ja nao tiver tido acoes suas compradas
            for a in range(len(possible[i])): #para cada dia
                dcompra = possible[i][a][0]
                dvenda = possible[i][a][1]
                simnao=[] #lista q armazena a resposta de se valores de dcompra ou dvenda passam ou nao no teste da cmaxvmaxintermediaria (ver for b in)
                for b in range(len(cmaxvmaxintermediaria)): #verifica se os dias ja foram utilizados no maior lucro passado
                    if dcompra == cmaxvmaxintermediaria[b][0] or dvenda == cmaxvmaxintermediaria[b][1]:
                        simnao.append("nao")
                    else:
                        simnao.append("sim")
                print(simnao)
                if "nao" not in simnao:
                    ifrodou=ifrodou+1
                    novolucro = master[i][dvenda-1]-master[i][dcompra -1]
                    if novolucro > lucro and novolucro>0: #verifica se o lucro computado e maior que o anterior
                        lucro=novolucro
                        print("NOVOLUCRO!= "+ str(novolucro)+" (da empresa "+ str(i)+")")
                        lastdcompramax = dcompra
                        lastdvendamax = dvenda
                        lastempresamax = i
    if lastdvendamax != 0 and lastdcompramax != 0:
        cmaxs.append(lastdcompramax) #lista de dias de compra maximos
        vmaxs.append(lastdvendamax) #lista de deias de venda maximos
        empresamaxs.append(lastempresamax) #lista de empresas cujo lucro foi maximo
    if cmaxs[0]==0:
        cmaxs.remove(0)
        vmaxs.remove(0)
    print (lucro)
    lucros.append(lucro)
    print (cmaxs)
    print (vmaxs)
    print ("if rodou: "+ str(ifrodou))
    print("endcall")
    '''if lucro!= 0:
        lucromax()
    '''
lucromax()
lucromax()
lucromax()
lucromax()

print(lucros)
print(empresamaxs)
"""esse print deve dar os lucros maximos em ordem decrescente.
"""
