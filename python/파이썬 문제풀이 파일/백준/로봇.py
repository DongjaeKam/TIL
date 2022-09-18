from platform import java_ver
import sys
sys.stdin = open("input.txt")

dir=((0,1),(-1,0),(0,-1),(1,0)) # 오른쪽 회전 기준 정리

M , n = map(int,input().split())

_index = 0
right_left = 1

i = 0
j = 0

for _ in range(n):

    command, number = input().split()

    num = int(number)

    if command == 'MOVE':
        if 0 <= i + dir[_index][0] * num <= M and 0 <= j + dir[_index][1] * num <= M :
            i+= dir[_index][0]*num
            j+= dir[_index][1]*num
        else:
            print(-1)
            break       
    else:
        if num == 0:
            _index +=3
            _index %= 4
        else :
            _index += 1
            _index %= 4
else:
    print(j, i)