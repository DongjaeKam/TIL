N = [input() for _ in range(0,8)]

tmp = 0

for i in range(0,4):
    for j in range(0,4):
      if N[i*2][j*2] == 'F':
            tmp+=1 

for i in range(0,4):
    for j in range(0,4):
      if N[i*2+1][j*2+1] == 'F':
            tmp+=1 

print(tmp)