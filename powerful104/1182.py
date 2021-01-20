import itertools as ite
a,b= map(int, input().split())
li = list(map(int, input().split()))
lit=[]
ans=0
for i in range(a):
    lit += ite.combinations(li,i+1)
for i in lit:
    if sum(i)==b:
        ans+=1
print(ans)