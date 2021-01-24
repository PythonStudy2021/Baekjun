s = input()
ans=10
exst=s[0]
for i in range(1,len(s)):
    if s[i]==exst:
        ans+=5
    else:
        ans+=10
    exst=s[i]
print(ans)