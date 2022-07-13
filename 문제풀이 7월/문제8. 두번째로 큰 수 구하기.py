numbers = [0, 20, 100, 50, -60, 50, 100]
max_index = 0
cnt = 1
M = 0

 

while True :
    M = numbers[0]
    max_index = 0
    for i in range(1,len(numbers) - cnt + 1):
        if M < numbers[i]:
            M = numbers[i]
            max_index = i

     
    tmp = numbers[max_index]
    numbers[max_index] = numbers[len(numbers)-cnt]
    numbers[len(numbers)-cnt] = tmp

    
    
    
    if cnt >= 2 and numbers[len(numbers)-cnt] < numbers[len(numbers)-1] :
        print(numbers[len(numbers)-cnt])
        break
        
    cnt+=1
    