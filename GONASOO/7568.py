N = int(input())

m = []
for i in range(N):
    X, Y = map(int, input().split())
    m.append([X, Y])

for i in m:
    r = 1
    for j in m:
        if i != m and i[0] < j[0] and i[1] < j[1]:
            r += 1
    print(r, end=' ')
