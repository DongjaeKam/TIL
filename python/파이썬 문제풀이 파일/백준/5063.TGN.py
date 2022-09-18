n = int(input())

for i in range(n):
    # 광고 x 광고 O 광고비용
    a, b, c  = map(int,input().split())
    tmp = b - a - c
    if tmp > 0:
        print("advertise")
    elif tmp == 0:
        print("does not matter")
    else :
        print("do not advertise")