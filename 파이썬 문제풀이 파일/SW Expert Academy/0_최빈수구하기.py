import sys

sys.stdin = open("_최빈수구하기.txt")

T = int(input())
 
for test_case in range(0,T):
    x = input()
    I =input().split()
    dic ={}
 
    for i in I:
        if i in dic:
            dic[i]+=1
        else :
            dic[i] = 1
 
    max_cnt = 0
    current_max =0
 

    #시험 제출 원본
    # for d in dic:
    #     if dic[d] >= max_cnt:
    #         max_cnt = dic[d]
    #         if int(d) >= current_max:  # ex) {'10': 10 } , {'1' : 11 } 인 경우에 오류가 생김
    #             current_max = int(d)
 
    #수정본
    
    for d in dic:
        if dic[d] >  max_cnt:
            max_cnt = dic[d] 
            current_max = int(d)
        elif dic[d] == max_cnt and int(d) > current_max:
            current_max = int(d)
        else:
            pass
      
    print(f"#{test_case+1} {current_max}")
