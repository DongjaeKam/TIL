n = int(input())
result = 'A'
result = 'B' if n < 0  and n % 2 == 1 else result
result = 'C' if n > 0  and n % 2 == 0 else result
result = 'D' if n > 0  and n % 2 == 1 else result
print(result)
