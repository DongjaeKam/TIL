n = int(input())
info = []
#입력 받기
for i in range(0,n):       # 키 몸무게를 저장하는 2차원 int 리스트 생성
    tmp = list(map(int,input().split()))
    info.append(tmp)
    

    
for i in range(0,n):
    cnt = 1
    for j in range(0,n):
        check0 = (info[i][0] < info[j][0]) #몸무게 비교
        check1 = (info[i][1] < info[j][1]) #키 비교
        
        if check0 and check1 :
            cnt+=1
        
        
    print(cnt, end = " ") 

