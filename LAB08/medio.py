masterlist = [[25, 2, 2, 4, 6],[21, 3], [20, 2, 4]]
#copy bellow
for i in masterlist:
    currentlist = i
    sum=0
    for a in range(len(currentlist)):
        sum = sum + currentlist[a]
    sum = sum - currentlist[0]
    medio = sum/(len(currentlist) - 1)
    currentlist.append(medio)
    i = currentlist
print (masterlist)
