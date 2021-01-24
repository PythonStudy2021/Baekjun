a, b, c= map(int, input().split())
rest=a+b
ans=0
while a>1 and b>0:
    if (rest-3)<c:
        break
    a=a-2
    b=b-1
    rest=a+b
    ans+=1
print(ans)