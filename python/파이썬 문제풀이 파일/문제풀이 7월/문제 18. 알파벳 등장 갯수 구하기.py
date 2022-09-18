word = 'banana'
Dic = {}
for w in word:
    if w.isalpha():
        if w in Dic :
            Dic[w] += 1
        else :
            Dic[w] = 1
for i in Dic :          
    print(i, Dic[i])