# 예제 10. [오류 해결] 더 큰 최댓값 찾기
#함수명을 변수명으로 사용했다. max를 변수명으로 쓰지말고 다른이름을 쓰면된다.
# 변수로 사용한 max를 모두 max1으로 변경
number_list = [1, 23, 9, 6, 91, 59, 29]
max1 = max(number_list)

number_list2 = [2, 5, 100, 20, 50, 10, 91, 82]
max2 = max(number_list2)

if max1 > max2:
    print("첫 번째 리스트의 최댓값이 더 큽니다.")

elif max1 < max2:
    print("두 번째 리스트의 최댓값이 더 큽니다.")