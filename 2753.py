year = int(input())
ans=0
if year%400==0:
    ans=1
elif year %100==0:
    ans=0
elif year % 4==0:
    ans=1
print(ans)