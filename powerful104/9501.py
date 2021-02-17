num=int(input())
for _ in range(num):
    ans=0
    tc, dist = map(int, input().split())
    for _ in range(tc):
        a, b, c = map(int, input().split())
        if b/c*a>=dist:
            ans+=1
    print(ans)