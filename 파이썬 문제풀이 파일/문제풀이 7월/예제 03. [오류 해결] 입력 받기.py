# 예제 03. [오류 해결] 입력 받기
# sum 에 string 변수를 넣은 경우 int로 정수로 변환
numbers = input().split()

numbers_int =list(map(int,numbers))

print(sum(numbers_int))