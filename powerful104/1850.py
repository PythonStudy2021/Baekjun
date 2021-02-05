from math import gcd as g
a,b= map(int, input().split())
for i in range(g(a,b)):
    print("1",end="")