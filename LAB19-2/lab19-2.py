

#board inputs working:
line1= input()
l= int(line1[0]+line1[1])
c= int(line1[3]+line1[4])
#print(l, c)


player1_Board=[[0 for i in range(c)]for j in range(l)]

for i in range(l):
    line=input()
    for j in range(c):
        player1_Board[i][j]=line[j]
#print(player1_Board)

player2_Board=[[0 for i in range(c)]for j in range(l)]

for i in range(l):
    line=input()
    for j in range(c):
        player2_Board[i][j]=line[j]
#print(player2_Board)



#recursive function:
#starting_Cell is [l, c]
#current_Boat is a list of [l, c] cells
def find_Neighbors(board, starting_Cell, current_Boat):
    i=starting_Cell[0]
    j=starting_Cell[1]
    if board[i-1][j]=='@':
        if [i-1, j] not in current_Boat:
            current_Boat.append([i-1, j])
            find_Neighbors(board, [i-1, j], current_Boat)
    if board[i][j-1]=='@':
        if [i, j-1] not in current_Boat:
            current_Boat.append([i, j-1])
            find_Neighbors(board, [i, j-1], current_Boat)
    if i+1<=l-1:
        if board[i+1][j]=='@':
            if [i+1, j] not in current_Boat:
                current_Boat.append([i+1, j])
                find_Neighbors(board, [i+1, j], current_Boat)
    if j+1<=c-1:
        if board[i][j+1]=='@':
            if [i, j+1] not in current_Boat:
                current_Boat.append([i, j+1])
                find_Neighbors(board, [i, j+1], current_Boat)
    return current_Boat #base case (all neighbors already in list or no neighbors)

#debugging find_Neighbors
#current_Boat=[[0, 2]]
#print(sorted(find_Neighbors(player1_Board, [0, 2], current_Boat)))
#print(len(find_Neighbors(player1_Board, [6, 18], current_Boat)))


#1. find player1 and player2 boats - WORKING

player1_Boats=[]
player2_Boats=[]

for i in range(l):
    for j in range(c):
        if player1_Board[i][j] =='@':
            boat=find_Neighbors(player1_Board, [i, j], [[i, j]])
            boat=sorted(boat)
            if boat not in player1_Boats:
                player1_Boats.append(boat)
for i in range(l):
    for j in range(c):
        if player2_Board[i][j] =='@':
            boat=find_Neighbors(player2_Board, [i, j], [[i, j]])
            boat=sorted(boat)
            if boat not in player2_Boats:
                player2_Boats.append(boat)

print(sorted(player1_Boats))
#print(len(player1_Boats))
#print(len(player2_Boats))

#2. scores

player1_Lives=len(player1_Boats)
player2_Lives=len(player2_Boats)


#3. attacks!
strikes=0 #debugging
while player1_Lives>0 and player2_Lives>0:
    s=input()
    player1_Attack=[int(s[0]+s[1]), int(s[3]+s[4])]
    for i in range(len(player2_Boats)):
        if player1_Attack in player2_Boats[i]:
            # update board
            for k in player2_Boats[i]:
                player2_Board[player2_Boats[i][k][0]][player2_Boats[i][k][1]]='-'
            # delete boat
            player2_Boats.remove(player2_Boats[i])
    strikes+=1
    if player2_Lives>0:
        s=input()
        player2_Attack=[int(s[0]+s[1]), int(s[3]+s[4])]
        for i in range(len(player1_Boats)):
            if player2_Attack in player1_Boats[i]:
                # update board
                for k in player1_Boats[i]:
                    player1_Board[player1_Boats[i][k][0]][player1_Boats[i][k][1]]='-'
                # delete boat
                player1_Boats.remove(player1_Boats[i])
    strikes+=1


#consertar o input de ataque pois variam os numeros de algarismos
