A = input().split()

A0=int(A[0][::-1])
A1=int(A[1][::-1])
output= A0 if A0>A1 else A1
print(output)