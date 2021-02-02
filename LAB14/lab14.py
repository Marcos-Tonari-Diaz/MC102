#lab14
#ler o input e formar a lista
#indicador de ordenacao: 0 (desordenado), c (crescente), d (decrescente)

l=input().split()
#F Ordenacao cresente - Insertion insertion sort

def OrdenacaoCrescente(l):
    for i in range(1, len(l)):
        keep=l[i]
        j=i-1
        while j>=0 and l[j]> keep:
            l[j+1]=l[j]
            j-=1
            #print(l)
        l[j+1]=keep
    return l

#F Ordenacao decresente - Insertion insertion sort reverso

def OrdenacaoDecrescente(l):
    for i in range(len(l)-1, -1, -1):
        keep=l[i]
        j=i+1
        while j<=len(l)-1 and l[j]> keep:
            l[j-1]=l[j]
            j+=1
            #print(l)
        l[j-1]=keep
    return l


#BB para lista crescente
def binarySearch_Crescente(x, l):
    m=[]
    start=0
    end=len(l)-1
    while start<=end:
        M=(start+end)//2
        m.append(str(M))
        if x==l[M]:
            print(" ".join(m)+" ")
            print("%s esta na posicao: %s"%(x, m[len(m)-1]))
            return
        else:
            if x>l[M]:
                start=M+1
            else:
                end=M-1
    print(" ".join(m)+" ")
    print("%s nao esta na lista!"%(x))
    return -1
#BB para lista decrescente
def binarySearch_Decrescente(x, l):
    m=[]
    start=0
    end=len(l)-1
    while start<=end:
        M=(start+end)//2
        m.append(str(M))
        if x==l[M]:
            print(" ".join(m)+" ")
            print("%s esta na posicao: %s"%(x, m[len(m)-1]))
            return
        else:
            if x>l[M]:
                end=M-1
            else:
                start=M+1
    print(" ".join(m)+" ")
    print("%s nao esta na lista!"%(x))
    return -1
#F inserir
def inserirCrescente(add, l):
    if len(l)==150:
        print("Limite de vagas excedido!")
        return -1
    if add in l:
        print("Aluno ja matriculado na turma!")
        return -1

    l.append(l[len(l)-1])
    for i in range(len(l)):
        if add<l[i]:
            break
    for j in range(len(l)-1, i, -1):
        l[j]=l[j-1]
    l[i]=add

def inserirDecrescente(add, l):
    if len(l)==150:
        print("Limite de vagas excedido!")
        return -1
    if add in l:
        print("Aluno ja matriculado na turma!")
        return -1

    l.append(l[len(l)-1])
    for i in range(len(l)):
        if add>l[i]:
            break
    for j in range(len(l)-1, i, -1):
        l[j]=l[j-1]
    l[i]=add

def inserirDesordenada(add, l):
    if add in l:
        print("Aluno ja matriculado na turma!")
        return -1
    l.append(add)
    
#F remover
def remover(rem, l):
    if l==[]:
        print("Nao ha alunos cadastrados na turma!")
        return -1
    elif rem not in l:
        print("Aluno nao matriculado na turma!")
    else:
        l.remove(rem)

#INTEGRACAO: funcao menu
indicador=0
ident=[1]
while ident[0] != 's':
    ident=input().split()
    if ident[0]=='p':
        if l!=[]:
            print(" ".join(l)+" ")
    if ident[0]=='c':
        OrdenacaoCrescente(l)
        indicador='c'
    if ident[0]=='d':
        OrdenacaoDecrescente(l)
        indicador='d'
    if ident[0]=='b':
        if indicador == 'c':
            binarySearch_Crescente(ident[1], l)
        elif indicador == 'd':
            binarySearch_Decrescente(ident[1], l)
        elif indicador == 0:
            print("Vetor nao ordenado!")
    if ident[0]=='i':
        if indicador == 'c':
            inserirCrescente(ident[1], l)
        elif indicador == 'd':
            inserirDecrescente(ident[1], l)
        elif indicador == 0:
            inserirDesordenada(ident[1], l)
    if ident[0]=='r':
        remover(ident[1], l)
    if ident[0]=='s':
        break
