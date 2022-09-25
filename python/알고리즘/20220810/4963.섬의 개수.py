from collections import deque


dj = [-1 ,-1,0,1,1,1,0,-1]
di = [0,1,1,1,0,-1,-1,-1]

while True:

    a , b = map(int,input().split())

    if a == 0 or b == 0:
        break 

    map_input = []
    map_check = []

    for i in range(b):
        tmp = list(map(int,input().split()))
        map_input.append(tmp)
        map_check.append(tmp)

    start_i = 0
    start_j = 0

    cnt = 0

    while True:

        break_check = False

        for i in range(b) :
            for j in range(a) :
                if map_check[i][j] != 0:
                    start_i = i
                    start_j = j
                    map_check[i][j] = 0
                    break_check = True
                    cnt+=1
                    break

            if break_check:
                break

        if break_check == False: #아무것도 탐색할 것이 없다.
            break

        arr = deque([])

        arr.append((start_i,start_j))

        while True:
            
            #print(arr)
            #print(f"cnt : {cnt}")

            tmp = arr.pop()

            for i in range(8):
                I = tmp[0]+di[i]
                J = tmp[1]+dj[i]

                if 0 <= I < b and 0 <= J < a :
                    if map_check[I][J] == 1:
                        arr.append((I,J))
                        map_check[I][J] = 0

            if len(arr) == 0:
                break


        

        # for i in range(b):
        #     for j in range(a):
        #         if map_check[i][j] == 1:
        #             print(1,end = "")
        #         else:
        #             print(0,end ="")
        #     print("")       

    #print(f"cnt : {cnt}")

    print(cnt)
