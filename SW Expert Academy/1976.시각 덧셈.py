T = int(input())

for i in range(0,T):
    H, M, h, m = map(int, input().split())
    
    output_h = H + h
    output_m = M + m
    if output_m > 60:
        output_m -= 60
        output_h += 1
    
    output_h%=12
    
    print(f"#{i+1} {output_h} {output_m}")