
a = int(input())
b = int(input())
c = int(input()) 
output = str(a*b*c)

d = list(str(a*b*c))
for i in range(10):
    print(d.count(str(i)))



'''
for i in range(0,10):
    cnt.append(0)

for i in output :
        cnt[ord(i)-ord('0')]+=1

for i in range(0,10) :
    print(cnt[i])

'''
 