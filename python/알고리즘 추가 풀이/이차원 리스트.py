dic = {}
a = {1:2 ,2:3 , 3:4}
b = {1:1 ,2:1}

dic = a

for i in b:
    if i not in dic:
        dic[i] = b[i]
    else:
        dic[i]+= b[i]


print(dic)