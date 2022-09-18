T = int(input())

for i in range(0,T):
    s = input()
    output = 1
    
    for j in range(0,len(s)//2):
            if s[j] != s[len(s)-j-1] :
                output = 0
                break;
                
    print(f"#{i+1} {output}")
