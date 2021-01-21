a,b= map(int, input().split())
ans=""
for _ in range(a):
    if len(ans)>b:
        ans=ans[:b]
        break
    ans+=str(a)
print(ans)