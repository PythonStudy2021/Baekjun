import sys
_N = int(input())
N = list(int(sys.stdin.readline()) for _ in range(_N))
for i in sorted(N): print(i)