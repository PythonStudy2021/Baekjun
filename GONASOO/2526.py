N, P = map(int, input().split())
n = N
k = []

while True:
    n = (n * N) % P
    if n in k:
        print(len(k[k.index(n):]))
        break
    k.append(n)
