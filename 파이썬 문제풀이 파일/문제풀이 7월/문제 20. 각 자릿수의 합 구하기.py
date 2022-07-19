n = int(input())
tmp = 0

while n!=0 :
    tmp+=(n%10)
    n//=10

print(tmp)
