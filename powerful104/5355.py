tc=int(input())
for _ in range(tc):
    li = input().split()
    ans=float(li[0])
    for i in range(len(li)-1):
        if li[i+1]=="@":
            ans*=3
        elif li[i+1]=="%":
            ans+=5
        else:
            ans-=7
    print("%.2f" %ans)