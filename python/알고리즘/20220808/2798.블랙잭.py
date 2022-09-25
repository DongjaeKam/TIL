n , m = map(int,input().split()) # 최댓값 카드 갯수 받기

cards = list(map(int,input().split())) #카드 값 받기

_max = 0 # 최대값을 비교하면서 저장



for i in range(0,n-2): #카드 3개기 때문에 카드 숫자 - 2까지
    if _max == m:
        break

    for j in range(i+1,n-1): # 2번째 카드는 [1번째 카드번호 + 1] 부터 카드 숫자-1 까지
        if _max == m:
            break

        for k in range(j+1,n): # 3번째 카드는 [2번째 카드번호 + 1] 부터 카드 숫자-1 까지
           
            tmp = cards[i] + cards[j] + cards[k] # 카드 세개 합 저장
            
            if m > tmp > _max:
                _max  = tmp
            
            elif tmp  == m:
               _max  = tmp
               break

print(_max)
