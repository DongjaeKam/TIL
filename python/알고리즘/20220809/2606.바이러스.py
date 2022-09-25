from collections import deque 

N = int(input())
M = int(input()) 

Matrix = [[] for i in range(N+1)]

for i in range(M):                          # M 개의 입력을 받으면서 M * M 행렬로 데이터 기록
    a , b = map(int,input().split())
    Matrix[a].append(b)
    Matrix[b].append(a)

infected_computer = 1

arr = deque([]) #큐를 쓰기 위해서 빈 행렬로 선언

check = [0 for i in range(N+1)] # 중복 작업 체크 및 갯수 세기용 리스트

for i in Matrix[infected_computer]: # 첫번째 것으로 초기화 
        check[i] = 1 #첫번째 것은 모두 감염이라서 모두 체크
        arr.append(i) # 큐에 감염된 것을 넣기


while len(arr)!=0:

    index = arr.pop()  # 감염된 것 하나 빼기

    for i in range(len(Matrix[index])): 
        num = Matrix[index][i] 
        
        if check[num] != 1: #감염 기록이 없는 경우 : 무한 루프 방지
            arr.append(num) # 옆에 감염된 것을 체크하기 위한 인덱스용 으로 저장
            check[num] = 1 #감염됬다는 것을 체크


print(sum(check)-1)