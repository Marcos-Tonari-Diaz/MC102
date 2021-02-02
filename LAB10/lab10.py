
#4 functions

originalstr=input() #imutavel (string)
print(originalstr)
texto=originalstr.split() #modificar!

#procura palavra em texto e retorna uma lista com TODAS as posicoes da palavra em ordem crescente
#FUNCIONANDO!
def search(word):
    textostr=' '.join(texto)
    textoref=textostr.lower().split()
    wordref=word.lower()
    returnlist=[]
    punctuation= ", . ? ! :".split()
    for i in range(len(punctuation)):
        punctuation[i]= wordref + punctuation[i]
    punctuation.append(wordref)
    for i in range(len(punctuation)):
        for j in range(len(textoref)):
            if punctuation[i] == textoref[j]:
                returnlist.append(j)

    return sorted(returnlist)


# d() FUNCIONANDO
def d():
    word=input()
    positions=search(word)
    positions.reverse()
    for i in positions:
        texto.pop(i)
    print(' '.join(texto))

# i() FUNCIONANDO
def i():
    word=input()
    positions=search(word)
    punctuation= ", . ? ! :".split()
    for i in positions:
        inv=""
        for x in texto[i]:
            inv= x + inv
        if inv[0] in punctuation:
            texto[i]=inv[1:len(inv)]+inv[0]
        else:
            texto[i]=inv

    print(' '.join(texto))

def r():
    word=input()
    replace=input()
    positions=search(word)
    punctuation= ", . ? ! :".split()
    for i in positions:
        if texto[i][len(texto[i])-1] in punctuation:
            texto[i]=replace + texto[i][len(texto[i])-1]
        else:
            texto[i]=replace
    print(' '.join(texto))





#menu (FUNCIONANDO)
identificador=0
while identificador != 'Q':
    identificador= input()
    if identificador == 'D':
        d()
    if identificador == 'I':
        i()
    if identificador == 'R':
        r()
