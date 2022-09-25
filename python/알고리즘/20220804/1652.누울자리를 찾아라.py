n = int(input())
s = [input() for i in range(n)]
rows_cnt = 0
columns_cnt = 0
total = 0
for i in range(0,n):
    tmp = 0
    for j in range(0,n):
        if s[i][j] == '.':
            tmp+=1
            if tmp == 2:
                rows_cnt+=1
        else:
               tmp = 0

for i in range(0,n):
    tmp = 0
    for j in range(0,n):
        if s[j][i] == '.':
            tmp+=1
            if tmp == 2:
                columns_cnt+=1
        else:
            tmp = 0

print(rows_cnt, columns_cnt)