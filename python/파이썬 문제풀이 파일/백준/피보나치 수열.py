n = int(input())
a = [1,1]

if n > 2:
    for i in range(2,n):
        a.append(a[i-1]+a[i-2])
    
print(a[n-1])