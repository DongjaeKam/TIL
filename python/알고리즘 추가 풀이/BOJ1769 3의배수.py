s = int(input())

def MultipleOfThree(_tuple):

    tmp = _tuple[1]
    N = 0 
    
    while tmp != 0:
        N += tmp%10
        tmp//=10


    if N < 10:
        return ( 1 , N)
    else :
        tmp = _tuple
        tmp[0] +=1
        tmp[1] = N
        return tmp

N = MultipleOfThree((0,s))

print(N[0])
if N[1] % 3 == 0:
    print("YES")
else:
    print("NO")

if N%3 == 0:
    print('YES')
else :
    print('NO')