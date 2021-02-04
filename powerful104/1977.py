li=[]
for i in range(1,101):
    li.append(i**2)
m = int(input())
n = int(input())
ra=list(range(m,n+1))
se=set(li) & set(ra)
if len(se)!=0:
    print(sum(se))
    print(min(se))
else:
    print(-1)