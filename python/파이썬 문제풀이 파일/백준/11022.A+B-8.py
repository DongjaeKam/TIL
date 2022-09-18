#11022
#Case #x: A + B = C
T = int(input())
for i in range(0,T):
    A, B = map(int,input().split())
    print(f'Case #{i+1}: {A} + {B} = {A+B}')
