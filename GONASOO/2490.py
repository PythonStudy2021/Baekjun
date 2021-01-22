for _ in range(3):
    N = list(input().split())
    r = chr(64+N.count('0'))
    if r == '@': r = 'E'
    print(r)