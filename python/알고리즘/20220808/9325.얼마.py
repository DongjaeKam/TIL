T = int(input())

for _ in range(0,T) :
    
    price_of_car = int(input())
    num_of_option = int(input())

    if num_of_option !=0:
        for _ in range(0,num_of_option):
            amount , price = map(int,input().split())
            price_of_car += amount*price

    print(price_of_car)