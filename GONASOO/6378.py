while True:
    N = int(input())
    if N == 0: exit()
    r = N
    while r >= 10:
        r = sum(map(int,list(str(N))))
        N = r
    print(r)