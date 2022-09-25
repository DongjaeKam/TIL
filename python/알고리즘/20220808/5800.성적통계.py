T = int(input())

for ClassNumber in range(1,T+1):
    _input = list(map(int,input().split()))[1:]
    Min = min(_input)
    Max = max(_input)
    LargestGap = 0
    s =sorted(_input)

    for i in range(0,len(s)-1):
        if s[i+1] - s[i] > LargestGap:
            LargestGap = s[i+1] - s[i]
    print(f"Class {ClassNumber}")
    print(f"Max {Max}, Min {Min}, Largest gap {LargestGap}")