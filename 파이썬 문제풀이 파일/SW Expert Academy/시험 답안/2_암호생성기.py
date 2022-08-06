import sys

sys.stdin = open("_암호생성기.txt")


for testcase in range(1,11):

    n = int(input())
    _input = list(map(int,input().split()))


    for i in range(0,len(_input)):
        _input[i] %=60




    while not ( 0 in _input):
        judgement = False

        tmp = []

        for i in range(1,6):
            if _input[0] > i :
                _input[0]-=i 
            else:
                _input[0] = 0

            tmp = _input[1:8]
            tmp.append(_input[0])
            _input = tmp

            if _input[7] == 0:
                judgement = True
                break

        if judgement :
            break
                
    print(f"#{testcase}" ,end =" ")            
    print(*_input)
