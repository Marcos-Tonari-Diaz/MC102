"""
LAB05
MArcos Gabriel B D Diaz
RA 221525
"""

ryuWins=0
kenWins=0
def round():
    HPryu = 2000
    HPken = 2000
    countneg= 0
    countpos= 0

    while HPryu >0 and HPken >0: #loop
        if countpos >= HPken:
            lastHP= HPken
            HPken= HPken - countpos
            print ("Ken: "+ str(lastHP)+" - "+ str(countpos)+" = "+ str(HPken))
            countpos= 0
        elif abs(countneg) >= HPryu:
            lastHP= HPryu
            HPryu= HPryu + countneg
            print ("Ryu: "+ str(lastHP)+" - "+ str(-countneg)+" = "+ str(HPryu))
            countneg= 0

        else:
            entrada = int(input())
            #AVANCADO EX
            entradafinal=0
            sum=0
            for i in range(1,entrada):
                sum=sum+i
                if sum==entrada:
                    entradafinal=entrada*2
                    break
                elif sum > entrada:
                    break
            sum=0
            for i in range(1,entrada):
                if entrada%i == 0:
                    sum=sum+i
                    if sum== entrada:
                        entradafinal=entrada*3
                        break
                    elif sum > entrada:
                        break
            if entrada < 0:
                entrada=abs(entrada)
                sum=0
                for i in range(1,entrada):
                    sum=sum+i
                    if sum==entrada:
                        entradafinal=-entrada*2
                        break
                    elif sum > entrada:
                        break
                sum=0
                for i in range(1,entrada):
                    if entrada%i == 0:
                        sum=sum+i
                        if sum== entrada:
                            entradafinal=-entrada*3
                            break
                        elif sum > entrada:
                            break
                entrada=-entrada
            if entradafinal != 0:
                entrada=entradafinal

            #TERMINA AVANCADO EX
            if entrada < 0:
                #salvar a adicao de dano de RYU
                countneg= countneg + entrada
                #imprimir o HP de KEN
                if countpos !=0:
                    lastHP= HPken
                    HPken= HPken - countpos
                    print ("Ken: "+ str(lastHP)+" - "+ str(countpos)+" = "+ str(HPken))
                    countpos= 0
            else:
                #salvar a adicao de dano de KEN
                countpos= countpos + entrada
                #imprimir o HP de RYU
                if countneg !=0:
                    lastHP= HPryu
                    HPryu= HPryu + countneg
                    print ("Ryu: "+ str(lastHP)+" - "+ str(-countneg)+" = "+ str(HPryu))
                    countneg= 0
    if HPryu <= 0:
        return 0
    if HPken <= 0:
        return 1

if round() == 0:
    kenWins=kenWins+1
else:
    ryuWins=ryuWins+1
if round() == 0:
    kenWins=kenWins+1
else:
    ryuWins=ryuWins+1


if ryuWins == 2:
    print ("Ryu venceu")
elif kenWins == 2:
    print ("Ken venceu")
else:
    print ("empatou")
