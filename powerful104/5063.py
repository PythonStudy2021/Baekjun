for _ in range(int(input())):
    a, b, c = map(int, input().split())
    if b-c>a:
        d="advertise"
    elif b-c==a:
        d="does not matter"
    elif b-c<a:
        d="do not advertise"
    print(d)