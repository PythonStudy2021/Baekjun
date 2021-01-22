num = int(input())
numa = int(input())
se=set()
li=[]
for _ in range(numa):
    a, b = map(int, input().split())
    li.append([min(a,b),max(a,b)])
li.sort()
se.add(1)
for _ in range(10):
    for i in li:
        if i[0] in se:
            se.add(i[1])
        elif i[1] in se:
            se.add(i[0])
print(len(se)-1)
