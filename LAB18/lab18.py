import sys
og=open(sys.argv[1], "r")
format=og.readline().split()
m, n = og.readline().split()
m=int(m)
n=int(n)
#print(m)
#print(n)
maxval=og.readline().split()
#print(maxval)
#print(og.readline().split())
ogmatrix= [og.readline().split() for j in range(n)]
for i in range(n):
    for j in range(m):
        ogmatrix[i][j]=int(ogmatrix[i][j])
#entry1 test
"""
#hack do carlos - funfando
for i in range(len(ogmatrix)):
    for j in range(len(ogmatrix[i])):
        if j==len(ogmatrix[i])-1:
            andy='\n'
        else:
            andy=' '
        print(ogmatrix[i][j],end=andy)
"""

og.close()
#print(" ")

#for i in range(len(ogmatrix)):
#    print(ogmatrix[i])


convolution=open(sys.argv[2], "r")
theD=int(convolution.readline())
nucleousMatrix= [convolution.readline().split() for i in range(3)]
for i in range(3):
    for j in range(3):
        nucleousMatrix[i][j]=int(nucleousMatrix[i][j])
#print(nucleousMatrix)
#print(theD)

#entry2 test
'''
for i in range(3):
    for j in range(3):
        if j==3-1:
            andy='\n'
        else:
            andy=' '
        print(nucleousMatrix[i][j],end=andy)
'''

convolution.close()

finalMatrix=[[0 for w in range(m)]for z in range(n)]

for i in range(n): #i: 0-[n-1]
    for j in range(m):
        if i==0 or j==0 or i==n-1 or j==m-1:
            finalMatrix[i][j]=ogmatrix[i][j]
        else:
            finalMatrix[i][j]=(nucleousMatrix[0][0]*ogmatrix[i-1][j-1]+nucleousMatrix[0][1]*ogmatrix[i-1][j]+nucleousMatrix[0][2]*ogmatrix[i-1][j+1]+nucleousMatrix[1][0]*ogmatrix[i][j-1]+nucleousMatrix[1][1]*ogmatrix[i][j]+nucleousMatrix[1][2]*ogmatrix[i][j+1]+nucleousMatrix[2][0]*ogmatrix[i+1][j-1]+nucleousMatrix[2][1]*ogmatrix[i+1][j]+nucleousMatrix[2][2]*ogmatrix[i+1][j+1])//theD


for i in range(n): #i: 0-[n-1]
    for j in range(m):
        if finalMatrix[i][j]<0:
            finalMatrix[i][j]=0
        elif finalMatrix[i][j]>255:
            finalMatrix[i][j]=255

print(format[0])
print(str(m)+" "+str(n))
print(maxval[0])
for i in range(len(finalMatrix)):
    for j in range(len(finalMatrix[i])):
        if j==len(finalMatrix[i])-1:
            andy='  \n'
        else:
            andy=' '
        print(finalMatrix[i][j],end=andy)
