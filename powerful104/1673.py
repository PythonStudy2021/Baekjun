while 1:
    try:
        a, b = map(int, input().split())
        c = a
        while a >= b:
            c += a // b
            a = a // b + a % b
        print(c)
    except EOFError:
        break