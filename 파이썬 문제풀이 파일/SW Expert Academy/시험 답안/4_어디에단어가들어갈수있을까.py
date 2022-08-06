import sys

sys.stdin = open("_어디에단어가들어갈수있을까.txt")

T = int(input())

for testcase in range(1,T+1):


    N , M = map(int,input().split())

    s = []

    arr =[]

    for i in range(0,N):
        s.append(list(map(int,input().split())))

    cnt = 0 

    for i in range(0,N):
        length = 0
        for j in range(0,N):
            if s[i][j] == 0:
                if length == M:
                    cnt+=1

                length = 0
            else :
                length += 1

        if length == M:
            cnt+=1     

    for i in range(0,N):
        length = 0
        for j in range(0,N):
            if s[j][i] == 0:
                if length == M:
                    cnt+=1

                length = 0
            else :
                length += 1

        if length == M:
            cnt+=1       


    print(f"#{testcase} {cnt}")