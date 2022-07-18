word = 'banana'
gap = ord('A') - ord('a') 
output =""
for w in word :
    output+=chr(ord(w)+gap)

print(output)