_min,_max =map(int,input().split())

cnt = 0


for i in range(_min,_max+1):
    n = 1
    while True:
        n+=1
        if n^2 > i:
            break
        else:
            if i%(n*n)== 0:
                cnt+=1
                break
        
        
print(_max-_min + 1 - cnt)
        
                
        