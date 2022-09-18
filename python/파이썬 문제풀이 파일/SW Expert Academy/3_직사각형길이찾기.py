import sys

sys.stdin = open("_직사각형길이찾기.txt")

T = int(input())
for i in range(0,T):    
    n = list(map(int,input().split()))
    length = 0
 
    if n[0] == n[1]:
        length = n[2]
    if n[0] == n[2]:
        length = n[1]
    if n[1] == n[2]:
        length = n[0]
    print(f"#{i+1} {length}")
