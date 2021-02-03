n = int(input())
x = []
x1 = 64
count = 1

while n < x1:
    x1 = int(x1 / 2)

x.append(x1)

while sum(x) != n:
    x1 = int(x1 / 2)
    if sum(x) + x1 <= n:
        x.append(x1)

print(len(x))