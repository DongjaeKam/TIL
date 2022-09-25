
n = int(input())
l = list(map(int,input().split()))

gap = []

for i in range(1,len(l)):
    gap.append(l[i]-l[i-1]) # 지점간의 높이 차이 저장

total = 0
Max = 0

for i in range(0,len(gap)):
    if gap[i] > 0:
        total+=gap[i] #지점간의 높이 차이를 계속 더한다

        if total > Max:
            Max = total # 가장 큰 값이 되면 저장
    else:
        total = 0 #내리막길이면 0으로 초기화 해서 다음을 준비
        
print(Max)


    

    
    