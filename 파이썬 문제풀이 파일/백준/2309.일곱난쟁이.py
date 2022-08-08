_input = []
for _ in range(9):
    _input.append(int(input()))
s = sum(_input) - 100

a = 0
b = 0
tmp = 0

_input.sort()


for i in range(0,9):
    if a!=0:
        break
    
    for j in range(i+1,9):
        tmp = _input[i]+ _input[j]
        if tmp == s:
            a = i
            b = j

for i in range(0,9):
    if i not in [a,b]:
        print(_input[i])


