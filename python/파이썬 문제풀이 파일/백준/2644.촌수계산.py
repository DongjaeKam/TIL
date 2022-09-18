n = int(input())
a , b = map(int,input().split())
m = int(input())

a_check = []
b_check = []

person = [[] for _ in range(n+1)]

for i in range(0,m):
    c, d = map(int,input().split())
    person[d].append(c)

num = a 

check1 = False

while len(person[num]) :
    a_check.append(person[num][0])
    if person[num][0] == b:
        check1 = True
        break
    num = person[num][0]

num = b

check2 = False

while len(person[num])!=0 :
    b_check.append(person[num][0])
    if person[num][0] == a:
        check2 = True
        break
    num = person[num][0]


if check1 == True :
    print(len(a_check))
elif check2 == True:
    print(len(b_check))
else:
    length = len(set(a_check)|set(b_check))-len(set(a_check)&set(b_check)) + 2 
    if len(set(a_check)&set(b_check)): # 공통조상의 수(아버지, 할아버지 ...)가 0이 아니면 
        print(length)
    else:
        print(-1)


