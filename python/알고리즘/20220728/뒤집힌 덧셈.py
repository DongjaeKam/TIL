n = input().split()

_sum =int(n[0][::-1])+int(n[1][::-1])
output = str(_sum)[::-1]

# _sum = 0

# d = 1

# for i in range(0,len(n[0])):
#     _sum += d*int(n[0][i])
#     d*=10

# d = 1

# for i in range(0,len(n[1])):
#     _sum += d*int(n[1][i])
#     d*=10

# output = str(_sum)

cnt = -1

while True:
    cnt+=1
    if output[cnt] != '0':
        break


print(output[cnt:])