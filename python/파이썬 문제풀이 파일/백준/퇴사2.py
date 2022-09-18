import sys
from collections import deque


sys.stdin = open("input.txt")

N = int(input())

input_arr = []
check =[True for i in range(N)]
_sum = 0


for i in range(N):
    n = list(map(int,input().split()))

    if n[0] + i - 1 < N:
        input_arr.append((n[0],n[1]))
    else:
        check[i]= False
        input_arr.append((0,0))

    print(input_arr)


for i in range(N):
    
    print(check)
    if check[i] == True:
        _sum = 0
       
        for j in range(1,input_arr[i][0]):
            _sum+=input_arr[i+j][1]
            
            
        if _sum < input_arr[i][1]:
            for j in range(input_arr[i][0]-1):
                check[i+j] = False


total = 0
        
for i in range(len(input_arr)):
    if check[i]:
        total += input_arr[i][1]


print(total)









