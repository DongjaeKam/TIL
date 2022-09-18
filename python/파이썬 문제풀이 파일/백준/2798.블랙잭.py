from operator import truediv

n , m = map(int,input().split())
cards = list(map(int,input().split()))
_max = 0
output = 0
checkj = False

for i in range(0,n-2):
    if _max == m:
        break

    for j in range(i+1,n-1):
        if _max == m:
            break

        for k in range(j+1,n):
            tmp = cards[i] + cards[j] + cards[k]
            if m > tmp > _max:
                _max  = tmp
            elif tmp  == m:
               _max  = tmp
               break

print(_max)
