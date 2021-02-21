from collections import Counter

_N = int(input()); N = Counter(map(int,input().split()))
_M = int(input()); M = list(map(int,input().split()))
for m in M: print(N[m], end=' ')