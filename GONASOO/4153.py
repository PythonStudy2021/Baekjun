while True:
    T = list(map(int,input().split()))
    if T == [0,0,0]: break
    T.sort()
    if T[-1]**2 == T[0]**2 + T[1]**2: r = "right"
    else: r = "wrong"
    print(r)