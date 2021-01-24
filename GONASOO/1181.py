N = int(input())
r = []
for _ in range(N):
    t = input()
    if not t in r: r.append(t)

r.sort()
r.sort(key=lambda x:len(x))

for i in r: print(i)