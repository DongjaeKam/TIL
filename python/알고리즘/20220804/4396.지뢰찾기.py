T = int(input())
map1 = []
map2 = []
map3 = [[0,0,0,0,0,0,0,0] for i in range(0,T)]

num = {1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",0:"0"}

for i in range(T):
    map1 += list(input().split())

for i in range(T):
    map2 += list(input().split())

check = True

for i in range(T):
    for j in range(8):
        if map1[i][j] == '*' and map2[i][j] == 'x':
            check = False
            break

    if check==False:
        for i in range(T):
            for j in range(0,8):
                print(map1[i][j],end = "")
        
            print("")
                
        break
    

if check :
    for i in range(T):
        for j in range(0,8):
            if map2[i][j] == 'x':
                cnt = 0

                for a in range(-1,2):
                    for b in range(-1,2):
                        if 0 <= i+a <T and 0<= j+b <8:
                            if map1[i+a][j+b] == '*':
                                cnt+=1; 
               
                map3[i][j] = cnt

            else :
                map3[i][j] = -1




    for i in range(T):
        for j in range(8):
            if map3[i][j] == -1:
                print('.',end="")
            else:
                print(f"{map3[i][j]}",end="")

        print("")

