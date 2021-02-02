N = int(input())
count=0
for i in range(N):
    line= []
    vl=i+1
    for a in range(1,N+1):
        dividendo= a
        if a % vl ==0 or vl % a==0:
            line.append("*")
            count=count+1
        else:
            line.append("-")
    str1= ''.join(line)
    print (str1)

print (count)
