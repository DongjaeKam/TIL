#import sys

#sys.stdin = open("_민석이의과제체크하기.txt")

testcase = 1

T = int(input())

for testcase in range(1,T+1):

    n,k = map(int,input().split()) 

    s = [0 for i in range(0,n)]

    p = list(map(int,input().split()))

    output = ""

    for i in range(1,n+1):
        if not(i in p):
            output+=f"{i} "

    print(f"#{testcase} {output}" ,end ="")

