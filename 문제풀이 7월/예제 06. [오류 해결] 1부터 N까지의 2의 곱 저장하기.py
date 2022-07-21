#예제 06. [오류 해결] 1부터 N까지의 2의 곱 저장하기
#배열을 사용할때는 () ← 이것이 아니라 []  ← 이것을 사용
N = 10
answer = []
for number in range(N + 1):
    answer.append(number * 2)

print(answer)