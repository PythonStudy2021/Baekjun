cy=100
sd=100
for _ in range(int(input())):
    a, b = map(int, input().split())
    if a>b:
        sd-=a
    elif a<b:
        cy-=b
print("%d\n%d"%(cy,sd))