import sys

sys.stdin = open("_신용카드만들기1.txt")


T = int(input())
 
for i in range( 0 , T ):
    s = input()
    tmp=s.replace('-','')
    if tmp[0] in ['3', '4', '5', '6', '9'] and len(tmp) == 16:
        print(f"#{i+1} 1")
    else:
        print(f"#{i+1} 0")