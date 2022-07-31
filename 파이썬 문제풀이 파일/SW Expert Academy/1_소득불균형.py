import sys

sys.stdin = open("_소득불균형.txt")

T = int(input())
for i in range(0,T):    
    N = input()
    income = list(map(int,input().split()))
    avg = sum(income)/len(income)
 
    cnt = 0
 
    for I in income :
        if I <= avg:
            cnt+=1
     
    print(f"#{i+1} {cnt}")
