word ='banana '
cnt = -1
for w in word:
    cnt+=1
    if w =='a':
           break;

            
if cnt == len(word) - 1 and word[len(word)-1]!='a' :
    cnt = -1
                    
            
print(cnt)