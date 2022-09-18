from collections import deque


n = int(input())
parent=list(map(int,input().split()))
node_num = int(input())


child = [[] for _ in range(n)]

for i in range(n):
    if parent[i]!=-1:
        child[parent[i]].append(i)



child[node_num] = []

_stack = deque([0])



cnt=0

if parent == [-1]:
    print(0)
else:
    while True:

        if len(_stack)!=0:
            _poped = _stack.pop()
            
        else:
            break

        if len(child[_poped]) == 0 and _poped!=node_num:
            cnt=cnt+1
        else:
            for c in child[_poped]:
                _stack.append(c)

    print(cnt)
    



