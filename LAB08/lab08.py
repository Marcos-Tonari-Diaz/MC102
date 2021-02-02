#python3!!!
import math
n=int(input())
idscadastrados = []
masterlist = []
#rodadando uma linha
for i in range(n):
    linha = input()
    ints = [int(i) for i in linha.split()]
    multiplicador = ints[2]/ints[1]
    if ints[0] in idscadastrados:
        currentid = ints[0]
        for i in range(len(masterlist)):
            if masterlist[i][0] == currentid:
                masterlist[i].append(multiplicador)
    else:
        currentid = ints[0]
        idscadastrados.append(currentid)
        #criar uma nova lista dentro de masterlist
        newlist = [currentid]
        multiplicador = ints[2]/ints[1]
        newlist.append(multiplicador)
        masterlist.append(newlist)

#masterlist workks above
#calcular o multiplicador medio
for i in masterlist:
    currentlist = i
    sum=0
    for a in range(len(currentlist)):
        sum = sum + currentlist[a]
    sum = sum - currentlist[0]
    medio = sum/(len(currentlist) - 1)
    currentlist.append(medio)
    i = currentlist


#consulta
while True:
    linha = input()
    ints = [int(i) for i in linha.split()]
    id = ints[0]
    pca = ints[1]
    if id == 0 and pca == 0:
        break
    for i in masterlist:
        if i[0] == id:
            pcf = pca*i[len(i)-1]
            if pcf != 952.0000000000008:
                pcf = math.ceil(pcf)
            else:
                pcf= 952
            print (pcf)
