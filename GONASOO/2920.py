N=list(map(int,input().split()));A=list(range(1,9));D=A[::-1]
if N==A: r="ascending"
elif N==D: r='descending'
else: r='mixed'
print(r)