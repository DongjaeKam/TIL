length = ord('z') - ord('a')
arr = []
_input=""
s = "1"

while len(s)!=0 :
    try : 
        s = input()
        _input+=s
    except:
        break

for i in range(length+1):
    tmp = chr(ord('a')+i)
    arr.append((tmp , _input.count(tmp)))


sorted_arr = sorted(arr,key = lambda x : -x[1])

check = sorted_arr[0][1]

for s in sorted_arr:
    if s[1] == check:
        print(s[0])
    else:
        break

