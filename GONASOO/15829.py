import sys

L = int(sys.stdin.readline())
S = sys.stdin.readline().strip()

r = 0
for i in range(L):
    r += (ord(S[i])-96) * (31 ** i)
print(r % 1234567891)
