K = int(input())
r = []
for i in range(K):
    t = int(input())
    if t == 0: r.pop()
    else: r.append(t)
print(sum(r))