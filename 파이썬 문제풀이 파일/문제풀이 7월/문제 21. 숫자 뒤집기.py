import math
n = int(input())
length = int(math.log10(n))+1
output = 0

for i in range(0,length):
    output +=((n%10)*pow(10,length-i-1))
    n//=10

print(output)

