
a=[]

class X:
    def __init__(self, nome, ra):
        self.nome= nome
        self.ra= ra

lilX=X("xis", 0000)
a.append(lilX)

a[0].nome="XIS"

lilX=X("Xis", 1111)
a.append(lilX)

print(lilX in a)
