for _ in range(int(input())):
    i, r = 0, 0
    S = list(input())
    for s in S:
        if s == 'O': i += 1; r += i
        else: i = 0
    print(r)