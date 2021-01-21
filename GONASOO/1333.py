N,L,D = map(int, input().split())
ck,d = 0,D

for _ in range(N):
    if ck<=d<ck+L:
        while d<ck+L:d+=D
    if ck+L<=d<ck+L+5: break
    ck+=L+5
print(d)