s = input()
N = [0,0,3,3,3,3,3,4,3,4]
_sum=[]
for i in range(0,10):
    _sum.append(sum(N[0:i+1]))

output = 0

for i in range(0,len(s)):
    tmp = ord(s[i])- ord('A') + 1
    j=0
    while True :
        j+=1
        if _sum[j] >= tmp:
            break
    
    output += j+1

print(output)


