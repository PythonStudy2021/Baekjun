import sys

N = int(input())
k = list(map(int, sys.stdin.readline().split()))
r = [0 for _ in range(N)]

for i in range(N):
    ct = 0
    for j in range(N):
        if r[j] == 0:
            if ct == k[i]:
                r[j] = i + 1
                break
            else: ct += 1

for i in r: print(i, end=' ')
