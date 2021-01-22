import sys
from collections import defaultdict
a,b= map(int, input().split())
sea={}
ans=[]
for _ in range(a+b):
    c = sys.stdin.readline().strip()
    sea.setdefault(c,0)
    sea[c]+=1
for i in sea.keys():
    if sea[i]==2:
        ans.append(i)
print(len(ans))
ans.sort()
for i in ans:
    print(i)