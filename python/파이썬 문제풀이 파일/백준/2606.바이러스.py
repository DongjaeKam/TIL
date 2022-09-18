from collections import deque 

N = int(input())
M = int(input())

tmp = [[] for i in range(N+1)]

for i in range(M):
    a , b = map(int,input().split())
    tmp[a].append(b)
    tmp[b].append(a)

infected_computer = 1

arr = deque([])

check = [0 for i in range(N+1)]

for i in tmp[infected_computer]:
        check[i] = 1
        arr.append(i)


while len(arr)!=0:

    index = arr.pop()

    for i in range(len(tmp[index])):
        num = tmp[index][i] 
        
        if check[num] != 1:
            arr.append(num)
            check[num] = 1


print(sum(check)-1)