n = list(map(int,input().split()))
A = input().split()
B = input().split()
SetA = set(A)
SetB = set(B)
SetI = SetA & SetB
SetU = SetA | SetB

print(len(SetU) - len(SetI))

