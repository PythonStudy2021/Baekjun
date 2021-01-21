N, M = map(int, input().split())

lN = len(str(N))

if lN*N <= M:
    for i in range(N):
        print(N, end='')
else:
    N = str(N)
    j = 0
    for i in range(M):
        if j == lN: j = 0
        print(N[j], end='')
        j += 1
