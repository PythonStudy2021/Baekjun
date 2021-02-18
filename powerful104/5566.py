n, m = map(int, input().split())
lin=[]
lim=[]
cur=0
ans=0
for _ in range(n):
    lin.append(int(input()))
for _ in range(m):
    lim.append(int(input()))
for i in lim:
    ans+=1
    cur+=i
    if cur>=n:
        break
    cur+=lin[cur]
    if cur>=n:
        break
        ans+=1
print(ans)