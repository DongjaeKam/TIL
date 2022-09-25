gap = ord('a')-ord('A')
def trans(char) :
    if ord(char) < ord('a'):
        return char
    else:
        trans = chr(ord(char) - gap)

    return trans

check = {}

I = input()

M = 0

for i in I:
    c = trans(i)
    if c in check:
        check[c] += 1
    else:
        check[c] = 1

    if check[c] > M:
        M = check[c]

output =""

for a in check:
    if check[a] == M :
        output = a if output == "" else "?"

print(output)
