num = int(input())
li=[]
for _ in range(num):
    li.append(list(map(int, input().split())))
n=0
plin=0
for i in range(num):
    s=set()
    for j in range(5):
        for k in range(num):
            if li[i][j]==li[k][j]:
                s.add(k)
    if n<len(s):
        n=len(s)
        plin=i
print(plin+1)