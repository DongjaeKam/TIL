n , k = list(map(int,input().split()))

def case_count(N):
    if N == 1 or N == 0:
        return
    else:
        
        for i in range(1,(N//2)+1):
            if result[i] != [] :
                for a in result[i]:
                    
                    if result[N-i] != [] :

                        for b in result[N-i]:
                            
                            dic = {}

                            for i in a: 
                                dic[i] = a[i]

                            for i in b:
                                if i not in dic:
                                    dic[i] = b[i]
                                else:
                                    dic[i]+= b[i]

                            

                            if not ( dic in result[N]) :
                                
                                tmp = 0
                                
                                for n in dic:
                                   tmp += n*dic[n]
                                
                                if tmp == N:   
                                    result[N].append(dic)


        if N in num:
            result[N].append({N:1})
        
        #print(result[N])


num = []


for i in range(n):
    num.append(int(input()))

result = [[] for _ in range(k+1)]


if 0 in num :
    result[0].append({0:1})  

if 1 in num:
    result[1].append({1:1})


for i in range(k+1):
    case_count(i)


output = 0


print(len(result[k]))
