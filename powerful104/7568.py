num = int(input())
li=[]
for _ in range(num):
    a, b = map(int, input().split())
    li.append((a,b))
for i in li:
    ans=1
    for j in li:
        if i[0]<j[0] and i[1]<j[1]:
            ans+=1
    print(ans,end=" ")