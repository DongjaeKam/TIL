s = input()
length = len(s)

i = 0

while i < (len(s) - 1):
    
    if i<(len(s)-1) :
        
        check1 = (s[i] in ['c','d' ] and s[i+1] == '-')
        check2 = (s[i] in ['c','s','z'] and s[i+1] == '=')
        check3 = (s[i] in ['l','n'] and s[i+1] == 'j')
        
        check = check1 or check2 or check3

        if check :
            length-= 1
            i+=1
        
    if i < (len(s)-2) :
        check = (s[i] == 'd' and s[i+1] =='z' and s[i+2] == '=')
        if check :
            length-=2
            i+=2
    i+=1
    
print(length)