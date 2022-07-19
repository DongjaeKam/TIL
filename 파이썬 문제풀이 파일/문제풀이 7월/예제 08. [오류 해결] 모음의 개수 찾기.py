# 예제 08. [오류 해결] 모음의 개수 찾기
# 조건문에서 0이 아닌 수는 모두 True , 그러므로 알파벳 한글자 같은 경우는 모두 True로 인식 
# 의도한 동작을 하려면 or 사이에 char == 을 각각 넣어줘야 한다.
word = "HappyHacking"

count = 0

for char in word:
    if char == "a" or char ==  "e" or char ==  "i" or char ==  "o" or char ==  "u":
        count += 1

print(count)