N , M = map(int,input().split())
Matrix =[]

for i in range(N+1):
    Matrix.append([0 for i in range(N+1)])

for _ in range(M):
    i , j = map(int,input().split())
    Matrix[i][j] = 1

arr = []

for i in range(N+1):
    tmp = []
    for j in range(N+1):
        if Matrix[i][j]!=0:
            tmp.append(j)

    arr.append(tmp)

print(Matrix)
print(arr)