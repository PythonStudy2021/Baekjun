num = int(input())
li = list(map(int, input().split()))
max=0
maxt=0
check=0
ma=-1001
for i in li:
    if i > 0:
        check=1
        break
    if ma<i:
        ma=i
if check==1:
    for i in range(0,num):
        maxt+=li[i]
        if max<maxt:
            max=maxt
        elif maxt<0:
            if i!=(num-1):
                maxt=0
    print(max)
else:
    print(ma)