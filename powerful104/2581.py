a = int(input())
b = int(input())
li=[]
for i in range(a,b+1):
    if i==1:
        continue
    check=0
    for j in range(2,i):
        if i%j==0:
            check=1
            break
    if check==0:
        li.append(i)
if(len(li)==0):
    print(-1)
else:
    print(sum(li))
    print(min(li))