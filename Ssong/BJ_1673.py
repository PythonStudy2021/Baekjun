while True:
    try:
        n, k = map(int, input().split())
        chicken = 0
        stamp = n
        while stamp >= k:
            tmp = 0
            while stamp >= k:
                stamp -= k
                tmp += 1
            stamp += tmp
            chicken += tmp
        chicken += n
        print(chicken)
    except EOFError:
        break