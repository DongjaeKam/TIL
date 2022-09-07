
survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]

_set = set([])
dic = {}

for s in survey:
    for a in s:
        _set+=a

for s in _set:
     dic[s] = 0

for i in range(len(survey)):
    
    tmp = choices[i]-4

    if tmp > 0:
        dic[survey[1]]+=tmp
    else:
        dic[survey[0]]-=tmp

    

    
print(answer)
