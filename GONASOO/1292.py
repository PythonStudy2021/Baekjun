A, B = map(int, input().split())
k = []
for i in range(1,46):
    for j in range(i):
        k.append(i)
print(sum(k[A-1:B]))
