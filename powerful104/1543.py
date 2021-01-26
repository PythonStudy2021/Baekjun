s = input().strip()
sf = input().strip()
ans=0

while s.count(sf)!=0:
    b = s[s.find(sf)+len(sf):]
    s=b
    ans+=1
print(ans)