from collections import deque

N , M = map(int,input().split()) # 정점의 개수 , 간선의 개수


cnt = 0

check = [0 for i in range(0,N+1)] # 중복 방문 방지 , 섬갯수 파악 

arr = [[] for i in range(0,N+1)] #그래프 관계정리

for _ in range(M):
    a,b = list(map(int,input().split()))
    arr[a].append(b)
    arr[b].append(a)

while True:

    num = 0

    for i in range(1,len(check)):
        if check[i] == 0 :
            num = i
            break

    tmp_stack = deque([])

    tmp_stack.append(num)
    check[num] = 1

    
    while True :
        
        tmp_pop = tmp_stack.pop() #맨위의 요소 출력 인덱스 역할
        
        for n in arr[tmp_pop]: #번호를 골라서
            if check[n] == 0:  #그게 나왔던 번호가 아니라면
                tmp_stack.append(n) #스택에 넣고
                check[n] = 1        #체크를 한다

        if len(tmp_stack) == 0: # 스택이 모두 비었을 경우 종료한다.
            break


    if sum(check) == N: #체크가 N 이라는 것은 모든요소를 체크했다는 것임으로
        print(cnt+1) # cnt+1을 한것을 출력한다. 
        break
    else:
        cnt+=1
 
    