import sys
sys.stdin = open("input.txt")

n = int(input())
_input =[]
for _ in range(n):
    _input.append(int(input()))

check= [0 for _ in range(n)]

total = _input[-1]
cnt = 1

for i in range(-2,-n-1,-1):
    if cnt == 0:
        total+=_input[i]
        cnt = 1
    elif cnt == 1:
        if i == -n:
            total+=_input[i]
        else:
            if _input[i] > _input[i-1]:
                total+=_input[i]
                cnt=2
            else:
                cnt = 0
    else:
        cnt = 0


print(total)





