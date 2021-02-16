ans=0
n=int(input())
li = list(map(int, input().split()))
b,c= map(int, input().split())
for i in li:
    i-=b
    if i>=0:
        if i%c==0:
            ans+=i//c
        else:
            ans+=i//c+1
print(ans+n)