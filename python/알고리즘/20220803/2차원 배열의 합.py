a , b = map(int,input().split())

arr = []

for i in range(a):
    arr.append(list(map(int,input().split())))

n = int(input())

for i in range(0,n):
    a,b,c,d = map(int,input().split())
    tmp = 0
    for i in range(a-1,c):
        for j in range(b-1,d):
            tmp+=arr[i][j]

    print(tmp)