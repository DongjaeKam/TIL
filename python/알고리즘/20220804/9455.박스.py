T = int(input())

for test_case in range(T):
    r , c = map(int,input().split())
    
    s = [list(map(int,input().split())) for i in range(0,r)]
    
    total = 0

    for j in range(0,c):
        cnt = 0

        for i in range(0,r):
            if s[i][j] == 1:
               cnt+=1
               total += (r-i-1)

        total-= cnt*(cnt-1)//2      

    print(total)

   