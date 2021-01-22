n,l,d = map(int, input().split())
t, pr = 0,d
for _ in range(n):
    if t<=pr and pr<t+l:
        while pr<t+l:
            pr+=d
    if t+l<=pr and pr<t+l+5:
        break
    t+=l+5
print(pr)