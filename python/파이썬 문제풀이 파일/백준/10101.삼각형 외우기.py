angle =[]
for i in range(3):
    angle.append(int(input()))

if sum(angle) == 180:
     length = len(set(angle))

     if length == 1:
        print("Equilateral")
     elif length == 2 :
        print("Isosceles")
     else :
        print("Scalene")
else:
    print("Error")