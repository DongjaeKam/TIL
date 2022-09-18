#import sys

#sys.stdin = open("_괄호짝짓기.txt")

from collections import deque

for testcase in range(1,11):

    n = int(input())
    S = input()
    K = deque([])

    dir = {')':'(','}':'{',']':'[','>':'<'}

    judgement = 1

    for s in S:
        if s in ['(','{','[','<']:
            K.append(s)
        elif K[-1] == dir[s] :
            K.pop()
        else:
            judgement = 0
            break

    print(f"#{testcase} {judgement}")

    