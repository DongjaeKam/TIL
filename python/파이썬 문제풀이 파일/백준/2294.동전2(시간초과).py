n , k = list(map(int,input().split()))
s =[]

for i in range(n):
    tmp = int(input())
    if not(tmp in s):
        s.append(tmp)

cnt = [0 for _ in range(len(s))]
s.sort(reverse=True)

check = False
total = 0
output = 0


while True:
    
    cnt[0]+=1
    
    for i in range(len(s)-1):
        if cnt[i] == s[i]+1:
            cnt[i] = 0
            cnt[i+1]+=1

    if cnt[-1] == (s[-1]+1):
        break

    total = 0

    for i in range(len(s)):
        total += (s[i]*cnt[i])


    print(cnt)

    if total == k:
        check = True
        output = sum(cnt)
        break

if check:
    print(output)
else:
    print(-1)