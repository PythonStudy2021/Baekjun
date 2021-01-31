r=31
m=1234567891
num=int(input())
s=input()
ans=0
for i in range(len(s)):
    ans+=((ord(s[i])-96)*(r**i))
print(ans%m)