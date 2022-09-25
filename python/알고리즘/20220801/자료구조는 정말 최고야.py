import sys
input = sys.stdin.readline

#deque 활용하지 않은 버전

a , n = map(int,input().split())

check = True


for i in range(0,n):
    num = input()
    arr = list(map(int,input().split()))
    
    for j in range(0,len(arr)):
        if j  != len(arr) - 1:
            if arr[j] < arr[j+1]:
                check = False
                
                
if check :
    print("Yes")
else :
    print("No")
                
        
'''
#deque 활용 버전

from collections import deque

total , lines = map(int,input().split())


dummy = []
p = []
for i in range(0,lines):
    tmp = input()
    dummy.append(deque(list(map(int,input().split()))))

for i in range(0,lines):
    p.append(0) 

check = 0
is_popped = True

while True :
    
    check+=1
    is_popped = False
    
    for i in range(0,lines):
        
        if p[i] == 0 and len(dummy[i])!=0:
            p[i] = dummy[i].pop()
         

        if p[i] == check:
            p[i] = 0
            is_popped = True

        check_zero = True

        for j in range(0,len(dummy)):
            if len(dummy[j]) != 0:
                check_zero = False
    
    if is_popped == False :
        break
    
    if check_zero:
        break
        
        
if is_popped :
    print("Yes")
else :
    print("No")


'''

