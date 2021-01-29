import sys
N,M = map(int,sys.stdin.readline().split())
C = list(map(int,sys.stdin.readline().split()))

mi = M
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            _mi = M - (C[i]+C[j]+C[k])
            if 0 <= _mi < mi: mi = _mi

print(M-mi)