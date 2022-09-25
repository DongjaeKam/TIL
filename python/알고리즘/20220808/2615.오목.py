board = []
X = 0
Y = 1

for _ in range(19):
    board.append(list(map(int,input().split())))




D = [(0,1),(1,0),(0,1),]

for i in range(0,19):
    for j in range(0,19):
        if board[i][j] != 0:
            tmpJ = j

            for d in D:
                tmpI =i d[X]
                tmpJ += d[Y]                 
                if 0 <= tmpI < 19 and 0 <= tmpJ < 19: 
                    if board[tmpI][tmpJ] == board[i][j]:
                        while board     



