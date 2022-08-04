T = int(input())

for i in range(0,T):
    arr = [0 for j in range(0,10)]
    
    n= int(input())
    cnt = 0
    while 0 in arr  :
        cnt+=1
        tmp =cnt * n
        
        while tmp!=0 :
            index = tmp%10
            arr[tmp%10]+=1
            tmp//=10
            
    print(f"#{i+1} {cnt*n}")