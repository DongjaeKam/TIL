s = input()
n = int(s)
check = 0

def sum_sit(n):
    total = 0
    while n!=0:
        total += n%10
        n//=10

    return total



if n > 20:
    cnt = n-9*(len(s))
else:
    cnt = 0

while True :

    cnt+=1

    if sum_sit(cnt) + cnt == n:
        check = 1            
        break

    if cnt == n :
        break


if check == 1:
    print(cnt)
else :
    print(0)

