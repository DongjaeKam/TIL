s = int(input())
result = 0
A = 0
B = 0
for i in range(1,s+1):
    #p 0 Q1  R2  S3 W4
    #A = WP
    #B = RQ + S(W-R)
    n = list(map(int,input().split()))
    A = n[4]*n[0]
    if n[2] > n[4]:
        B = n[1]
    else:
        B = n[1] + n[3]*(n[4]-n[2])
    
    if A<B :
        result = A
    else :
        result = B
    
    print(f"#{i} {result}")