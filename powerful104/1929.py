a,b= map(int, input().split())
li = set(range(2,b+1))
for i in range(2, b+1):
    if i in li:
        li -= set(range(2*i,b+1,i))
li-=set(range(a))
li=list(li)
li.sort()
for i in li:
    print(i)