import itertools as ite
a,b = map(int, input().split())
lit = list(map(int, input().split()))
li = ite.combinations(lit,3)
max=0
for i in li:
    sua=sum(i)
    if sua <= b and sua>max:
        max=sua
print(max)