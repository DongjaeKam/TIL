vowels = ['a','e','i','o','u','A','E','I','O','U']

while True:
    
    cnt = 0

    s = input()
    
    if s == "#" :
        break
    else:
        for a in s:
            if a in vowels:
                cnt+=1

    print(cnt)
