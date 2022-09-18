A,B,C = input().split(" ")
a = int(A)
b = int(B)
c = int(C)
result = (a if a<b else b) if ((a if a<b else b)<c) else c
print(int(result))
