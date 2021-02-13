def conv(k,m):
    r = ""
    while True:
        a = k % m
        k //= m
        r = str(a) + r
        if k < m: r = str(k) + r
        if k//m < 1: return int(r)


n = int(input()); flag = True
for i in range(2,11):
    t = str(conv(n, i))
    if t[::-1] == t:
        print(i, t)
        flag = False

if flag: print("NIE")