n, k= input().split()
n=int(n)
k=int(k)

matrix=[input().split()for i in range(n)]

#print(matrix)

def bubblesort(l):
    lista=l[:]
    for j in range(len(lista)):
        for i in range(len(lista)-1-j):
            if lista[i]>lista[i+1]:
                lista[i], lista[i+1]= lista[i+1], lista[i]
        #print(lista)
    return lista


def hier(hierChain, boss):
    #print("boss is "+ str(boss))
    #print("start:", hierChain)
    currentBossSubordinates=[] #line
    for j in range(len(matrix[boss])):
        currentBossSubordinates.append(matrix[boss][j])
    if '1' not in currentBossSubordinates: #base case
        #print("case")
        return hierChain
    else: #step
        #print("step")
        newBosses=[]
        for z in range(len(currentBossSubordinates)):
            if currentBossSubordinates[z]=="1" and z not in hierChain:
                hierChain.append(z)
                newBosses.append(z)
        #print("appended: ",hierChain)
        for r in range(len(newBosses)):
            hier(hierChain, int(newBosses[r]))
    return hierChain




hierChain=[k]
answer=hier(hierChain, k)
hierChain2=bubblesort(hierChain[1:])
hierChain=hierChain[0:1]+hierChain2
for i in range(len(hierChain)):
    hierChain[i]=str(hierChain[i])
#print(hierChain)
print(" ".join(hierChain))
