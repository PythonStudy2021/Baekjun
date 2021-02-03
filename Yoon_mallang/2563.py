n = int(input())
y = []
z = []
total = 0
for i in range(100):
    for j in range(100):
        y.append(0)
    z.append(y)
    y = []

for i in range(n):
    x_, y_ = map(int, input().split())
    for j in range(10):
        for k in range(10):
            z[x_ + j][y_ + k] = 1

for i in range(100):
    total = total + sum(z[i])

print(total)