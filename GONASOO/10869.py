A,B=map(int,input().split())
R = [A+B, A-B, A*B, A//B, A%B]
for r in R: print(r)