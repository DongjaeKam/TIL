n = []
for i in range(0,5):
    n.append(list(map(int,input().split()))) 

index = 0
_max = 0

cnt = 0

for a in n:
    cnt+=1
    s = sum(a)
    if s > _max:
        _max = s
        index = cnt


print(index , _max)  