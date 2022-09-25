T = int(input())

for _ in range(0,T):
    a , b = map(int,input().split())

    total = 0

    for i in range(a,b+1):
        s = str(i)
        total += s.count('0')

    print(total)
