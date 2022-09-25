n = list(map(int, input().split()))
_gcd = 1
_lcm = 1

while True :
    if n[0]%2 == 0 and n[1]%2 == 0: 
        n[0] //= 2
        n[1] //= 2
        _gcd*=2
    else:
        break

while n[0]%2 == 0:
    n[0]//=2
    _lcm*=2

while n[1]%2 == 0:
    n[1]//=2
    _lcm*=2

odd_number = 1

while True:
    odd_number+=2
    
    if n[0]%odd_number == 0 and n[1]%odd_number == 0:
        n[0]//= odd_number
        n[1]//= odd_number
        _gcd*=odd_number
    else:
        odd_number+=2

    if n[0] == 1 or n[1] == 1 :
            break;



_lcm=_lcm*_gcd*n[0]*n[1]

print(_gcd)
print(_lcm)