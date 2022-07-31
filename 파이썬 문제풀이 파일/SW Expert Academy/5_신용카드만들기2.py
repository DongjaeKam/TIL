import sys

sys.stdin = open("_신용카드만들기2.txt")

# 1) 홀수 자리 수 (4 x 2) + (2 x 2) + (0 x 2) + (0 x 2) + (1 x 2) + (0 x 2) + (4 x 2) + (6 x 2)
# 2) 짝수 자리 수 5 + 0 + 2 + 0 + 9 + 0 + 1 
# 3) N을 제외한 1) 과 2)를 더한 합은 51이므로 N의 값은 9입니다.
 
T = int(input())
 
for i in range(0,T):
    s = list(map(int,input().split()))
 
    _sum = 0
 
    for j in range(0,len(s)):
        if j%2 == 1:
            _sum+=s[j]
        else:
            _sum+=s[j]*2
 
    output = 10 - (_sum%10)
    output = output if output < 10 else 0
 
    print(f"#{i+1} {output}")