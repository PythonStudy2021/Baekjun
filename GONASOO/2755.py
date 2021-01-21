n = int(input())

C = 0.0
G = 0.0

def grade(x):
    return {'A+': 4.3,
            'A0': 4.0,
            'A-': 3.7,
            'B+': 3.3,
            'B0': 3.0,
            'B-': 2.7,
            'C+': 2.3,
            'C0': 2.0,
            'C-': 1.7,
            'D+': 1.3,
            'D0': 1.0,
            'D-': 0.7,
            'F': 0.0,
            }.get(x, -1.0)


for _ in range(n):
    s, c, g = map(str, input().split())
    C += float(c)
    G += grade(g) * float(c)


print('%.02f' % (G / C +0.000000000001))