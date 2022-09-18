# 예제 09. [오류 해결] 과일 개수 구하기
# 딕셔너리 값 추가 방법 오류 
# 딕셔너리 값 추가시에는  딕셔너리명[키값] = '키에 대응되는 값' 형식으로 추가해야 한다.
from pprint import pprint


fruits = [
    "Soursop",
    "Grapefruit",
    "Apricot",
    "Juniper berry",
    "Feijoa",
    "Blackcurrant",
    "Cantaloupe",
    "Salal berry",
]

fruit_count = {}

for fruit in fruits:
    if fruit not in fruit_count:
        fruit_count[fruit] = 1
    else:
        fruit_count[fruit] += 1

pprint(fruit_count)