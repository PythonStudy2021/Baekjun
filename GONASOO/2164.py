import sys as s
from collections import deque

_N = int(s.stdin.readline())
N = deque(range(1,_N+1))

for _ in range(_N-1):
    N.popleft()
    N.append(N.popleft())

print(N[0])
