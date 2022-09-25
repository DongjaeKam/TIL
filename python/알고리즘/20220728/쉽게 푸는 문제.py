a,b =map(int,input().split())

cnt = 1
_sum = 0
for i in range(1,b+1):
    if cnt*(cnt+1)//2 < i :
        cnt+=1
    _sum += cnt

    
cnt = 1

for i in range(1,a):
    if cnt*(cnt+1)//2 < i :
        cnt+=1

    _sum-=cnt

   
print(_sum)