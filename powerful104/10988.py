s=input()
ans=1
for i in range(len(s)//2):
    if s[i]!=s[-(1+i)]:
        ans=0
print(ans)