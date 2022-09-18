import sys

sys.stdin = open("달란트2.txt")

T = int(input())

for testcase in range(1,T+1):
    a , b = list(map(int,input().split()))

    _max = 0
    tmp = 0

    for j in range(b):
        A = a-j
        B = b-j 

        _mod = A%B 
        _mean = A//B

        tmp = 1

        if A%B == 0 :
            tmp *= (A//B)**B
        else :

            if _mod < _mean :
                
                for i in range(_mod):
                    tmp *= (_mean + 1)
                
                for i in range( B - _mod ):
                    tmp *= _mean
            
        _max = max(_max,tmp)


    print(f"#{testcase} {_max}")