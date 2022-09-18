a = input()
b = input()

output= 0 
cnt = 0
while cnt + len(b) <= len(a) :
     if a[cnt:cnt+len(b)] == b:
        output+=1
        cnt+=len(b)
     else:
        cnt+=1


print(output)