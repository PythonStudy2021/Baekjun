num = int(input())
for _ in range(num):
    h, w, n = map(int, input().split())
    c=n%h
    d=n//h+1
    if c==0:
        c=h
        d=n//h
    print("%d%02d" %(c, d))