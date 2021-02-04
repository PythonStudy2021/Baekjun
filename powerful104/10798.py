li=[]
max=0
for _ in range(5):
    s=input().strip()
    if max<len(s):
        max=len(s)
    li.append(s)
for i in range(max):
    for j in range(5):
        if len(li[j])>i:
            print(li[j][i],end="")