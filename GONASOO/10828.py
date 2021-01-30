import sys


def stack(s, o, t=0):
    rt = 0
    if o == 'push': s.append(t)
    elif o == 'pop':
        if s: rt = s.pop()
        else: rt = -1
    elif o == 'size': rt = len(s)
    elif o == 'empty':
        if s: rt = 0
        else: rt = 1
    else:  # top
        if s: rt = s[-1]
        else: rt = -1

    if o != 'push': print(rt)


S = []
for _ in range(int(sys.stdin.readline())):
    O = list(sys.stdin.readline().split())
    if len(O) == 2: stack(S, O[0], int(O[1]))
    else: stack(S, O[0])
