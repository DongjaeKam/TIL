s = []
for i in range(0,10):
    n = int(input())
    s.append(n)

i = 0

pre_total = 0
current_total =0
output = 0


while i < 10 :
    
    pre_total = current_total
    current_total += s[i]

    if current_total >= 100 : 
        break
    
    i+=1

gap_pre = 100 - pre_total
gap_current = current_total - 100

if gap_current <= gap_pre :
    output = current_total
else:
    output = pre_total    


print(output) 
