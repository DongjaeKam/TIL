import sys

sys.stdin = open("_문자열의거울상.txt")

T = int(input())
dic = {'d':'b', 'b':'d', 'p':'q', 'q':'p'}
 
for i in range( 0 , T ):
    S = input()
    tmp =""
    for s in S:
        tmp += dic[s]
     
    print(f"#{i+1} {tmp[::-1]}")