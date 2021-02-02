#LAB11
#etrada - FUNCIONANDO
size= input().split()
m=int(size[0])
n=int(size[1])
days=int(input())
matrix=[]
for i in range(m):
    matrix.append(input().split())
#inserting "0"s border - FUNCIONANDO
for i in range(m):
    matrix[i].insert(0, "0")
    matrix[i].append("0")
matrix.insert(0, ["0" for i in range(n+2)])
matrix.insert(len(matrix), ["0" for i in range(n+2)])
#copying a 2 dimensional list is hard!!!
modified= [i[:] for i in matrix]
#test matrix
#python3for a in range(len(matrix)):
#  print(matrix[a])

#function: returnvizinhos - FUNCIONANDO
#indices a(ij) NAO indices da lista!!! (começa no 1,1)
def returnvizinhos(i, j):
    return [matrix[i-1][j-1], matrix[i-1][j], matrix[i-1][j+1], matrix[i][j-1], matrix[i][j+1], matrix[i+1][j-1], matrix[i+1][j], matrix[i+1][j+1]]
#print(returnvizinhos(1, 1))

#working for 1 iteration!!!
def day(d):
    for i in range(1, m+1):
        for j in range(1, n+1):
            #print(matrix[i][j])
            #birth
            if matrix[i][j]=="0":
                v =returnvizinhos(i, j)
                if "1" in v:
                    v.remove("1")
                    if "1" in v:
                        v.remove("1")
                        if "1" not in v:
                            modified[i][j]="1"
            #infection
            elif matrix[i][j]=="1":
                if "2" in returnvizinhos(i, j):
                    modified[i][j]="2"

            #defeat or hunger
            elif matrix[i][j]=="2":
                v =returnvizinhos(i, j)
                #hunger
                if "1" not in v:
                    modified[i][j]="0"
                #defeat
                elif "1" in v:
                    v.remove("1")
                    if "1" in v:
                        modified[i][j]="0"
    '''
    print("matrix")
    for a in range(1, m+1):
        #matrix[a].pop(0)
        #matrix[a].pop()
        print(''.join(matrix[a][1:len(matrix[a])-1]))
    '''
    print("iteracao "+str(d+1))
    for a in range(1, m+1):
        #modified[a].pop(0)
        #modified[a].pop()
        print(''.join(modified[a][1:len(matrix[a])-1]))
print ("iteracao 0")
for c in range(1, m+1):
    print(''.join(matrix[c][1:len(matrix[c])-1]))
for d in range(days):
    day(d)
    matrix= [i[:] for i in modified]

#for i in range(days):
#    day()
#    matrix=modified
