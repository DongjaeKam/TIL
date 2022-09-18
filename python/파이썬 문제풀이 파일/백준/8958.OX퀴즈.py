n = int(input())
for i in range(0,n):
    s = input()
    j = 0
    tmp = 0
    total = 0
    while j < len(s):
        if s[j] == 'X':
            tmp = 0
        else :
            tmp += 1
            total+=tmp

        j+=1
    
    print(total)
