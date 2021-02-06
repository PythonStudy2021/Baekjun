num = int(input())
li = list(map(float, input().split()))
ma=max(li)
ans=0
for i in li:
    ans+=i/ma
print(ans/num*100)