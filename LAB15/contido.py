def contido(conj1, conj2):
    # Implementar a funcao e trocar o valor de retorno
    for i in range(len(conj1)):
        print (conj1[i])
        if conj1[i] not in conj2:
            return False
    return True
print(contido([1, 2, 3], [1, 2, 3, 4, 5]))
print(contido([1, 2, 8], [1, 2, 3, 4, 5]))
