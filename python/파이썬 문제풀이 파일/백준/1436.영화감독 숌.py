_input = int(input())
number = 0
num = 666

while True:
    
    s = str(num)

    if '666' in s:
        number+=1
    
    if number == _input:
        break

    num+=1   
 
print(num)    


