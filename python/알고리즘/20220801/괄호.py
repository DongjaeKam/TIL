from collections import deque 


N = int(input())

for i in range(0,N) :
    check = True
    PS = input() 
    container = deque([])

    for p in PS: 
        if p == "(" : 
            container.append(p)
        else :
            if len(container) != 0:
                container.pop()
            else :
                check = False

   
    if check and len(container) == 0:
         print("YES")
    else :
         print("NO")
