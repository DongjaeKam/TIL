from collections import deque
while True :
    _input = input()

    if _input == ".":
        break

    check = 0

    tmp = deque()

    for s in _input:
        
        if s == '(' or s == '[':
            tmp.append(s)
        elif s ==')':
            if len(tmp) == 0:
                    check = 1
                    break
        
            if tmp[len(tmp)-1] == '(':
                    tmp.pop()
            else :
                    check = 3
                    break
        elif s == ']':
            if len(tmp) == 0:
                check = 4
                break
            
            if tmp[len(tmp)-1] == '[':
                tmp.pop()
            else :
                check = 5
                break

    if check == 0 :
        print("yes")
    else :
        print("no")

    #print(check)