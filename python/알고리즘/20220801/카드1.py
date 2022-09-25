from collections import deque

n = int(input())

q = deque(range(1,n+1))

while len(q) != 1 :
    tmp = q.popleft()
    print(tmp,end =" ")
    tmp = q.popleft()
    q.append(tmp)

print(q[0])