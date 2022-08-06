import sys

sys.stdin = open("_파리퇴치.txt")

T = int(input())

for testcase in range(1,T+1):

    M,N = map(int,input().split())
    _input =[]

    for _ in range(0,M):
        _input.append(list(map(int,input().split())))


    _max = 0

    for a in range(0,M-N):

        for b in range(0,M-N):

            total = 0

            for i in range(0,N):
                for j in range(0,N):
                    total+=_input[i+a][j+b]

            _max = max(_max,total)

    print(f"#{testcase} {_max}")