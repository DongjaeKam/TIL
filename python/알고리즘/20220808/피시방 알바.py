N = int(input())
p = list(map(int,input().split()))

seat =[0 for _ in range(100)]
check = 0

for i in range(N):
    index = p[i]
    if seat[index-1] == 1:
        check+=1
    else:
        seat[index-1] = 1

print(check)

