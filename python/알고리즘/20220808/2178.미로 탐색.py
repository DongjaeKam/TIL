from collections import deque

r,c = map(int,input().split())

map1 = []

for _ in range(r):
    map1.append(input())

# for i in range(4):
#     for j in range(6):
#         print(map1[i][j],end ="")
#     print("")




map_check =[]

for i in range(r):
    tmp = []
    for j in range(c):
        if map1[i][j] == '0':
            tmp.append(-1)
        else:
            tmp.append(0)
    map_check.append(tmp)

# for i in range(4):
#     for j in range(6):
#         print(map_check[i][j],end ="")
#     print("")




dx = [-1,0,1,0]
dy = [0,1,0,-1]

start_point = (0,0)

map_check[0][0] = 1

arr = deque([start_point])

while len(arr)!=0 :
    tmp = arr.pop()

    tmpx = tmp[0]
    tmpy = tmp[1]

    if not(tmpx == c-1 and tmpy == r-1) :
        for i in range(4):
            x = tmpx + dx[i]
            y = tmpy + dy[i]

            if not(x >= c or x < 0 or y >=r or y < 0)and map_check[y][x]==0:
                arr.append((x,y))
                map_check[y][x] = map_check[tmpy][tmpx]+1






# for i in range(4):
#     for j in range(6):
#         print(map_check[i][j],end ="")

#     print("")


_min = r*c+1


# for i in range(r):
#         for j in range(c):
#             print(map_check[i][j],end ="")

#         print("")


if min(map_check[r-2][c-1],map_check[r-1][c-2]) == -1:
    map_check[r-1][c-1] = max(map_check[r-2][c-1],map_check[r-1][c-2])+1
else:
    map_check[r-1][c-1] = min(map_check[r-2][c-1],map_check[r-1][c-2])+1

print(map_check[r-1][c-1])


