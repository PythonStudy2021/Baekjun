num=int(input())
numtmp=num
ans=0
while True:
    ans+=1
    a = num // 10
    b = num % 10
    num=b*10+(a+b)%10
    if numtmp==num:
        break
print(ans)