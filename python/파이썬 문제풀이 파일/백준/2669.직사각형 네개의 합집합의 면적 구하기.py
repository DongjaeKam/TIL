A =set([])
for K in range(4):
    a,b,c,d =map(int,input().split())
    for i in range(a+1,c+1):
        for j in range(b+1,d+1):
                A.add((i,j))

print(len(A))



