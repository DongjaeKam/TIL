A =[]
B =[]

for i in range(10):
    A.append(int(input()))

for i in range(10):
    B.append(int(input()))

A_sorted = sorted(A,key = lambda x : -x)
B_sorted = sorted(B,key = lambda x : -x)

print(sum(A_sorted[:3]),end = " ")
print(sum(B_sorted[:3]))