from math import gcd

N = list(map(int, input().split()))
A, B = max(N), min(N)
print(gcd(A, B))
print(A*B//gcd(A, B))
