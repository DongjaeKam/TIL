#import sys

#sys.stdin = open("_조교의성적매기기.txt")


T = int(input())

score = {0 :"A+",1 :"A", 2 :"A-",3 :"B+",4 :"B0", 5 :"B-",6 :"C+",7 :"C0", 8 :"C-",9:"D0"}

for testcase  in range(1,T+1):
    n , k = map(int,input().split())

    k-=1

    student =[]

    for i in range(n):
        a ,b ,c = map(int,input().split())
        student.append([i+1,a*35 + b*45 + c*20,""])

    s = sorted(student,key = lambda x : -x[1] )

    n2 = n//10

    for i in range(0,n//n2):
        for j in range(0,n2):
            s[i*n2+j][2] = score[i]

    s2 = sorted(s,key = lambda x : x[0])

    print(f"#{testcase} {s2[k][2]}")