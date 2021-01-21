n = list(range(1, 11))

while True:
    o = int(input())
    if o == 0:
        exit()
    s = input()

    if s == "too high":
        for i in range(o-1, 10):
            n[i] = 0
    elif s == "too low":
        for i in range(0, o):
            n[i] = 0
    else:
        if o in n:
            print("Stan may be honest")
        else:
            print("Stan is dishonest")
        n = list(range(1, 11))

