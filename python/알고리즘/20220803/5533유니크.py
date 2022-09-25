N = int(input())
s = [list(map(int,input().split())) for _ in range(0,N)]
_sum =[]

for i in range(N):
    for j in range(3):
        for k in range(N):
            if k!=i and s[i][j] == s[k][j]:
                s[i][j] = 0
                s[k][j] = 0

for i in range(N):
    print(sum(s[i]))
