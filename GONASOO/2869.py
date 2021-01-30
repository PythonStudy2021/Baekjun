import sys
A,B,V = map(int,sys.stdin.readline().split())
r = (V-A)//(A-B)
k = r * (A-B)
while True:
    k += A
    r += 1
    if k >= V: break
    k -= B
print(r)

