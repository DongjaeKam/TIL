a , b = map(int,input().split())

# 세로 위치 a%4 + 3
# 가로 위치 a//4 + 1
output = abs(a%4 - b%4) + abs(a//4-b//4)
print(output)
