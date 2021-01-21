d = []
sum = 0
brk = False

for i in range(9):
    d.append(int(input()))
    sum += d[i]
d.sort()

for i in range(9):
    for j in range(i+1, 9):
        if (sum-(d[i]+d[j])) == 100:
            d.pop(i)
            d.pop(j-1)
            brk = True
            break
    if brk: break

for i in range(7):
    print(d[i])
