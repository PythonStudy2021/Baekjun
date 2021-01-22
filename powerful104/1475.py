li = list(map(int, list(input())))
ans=0
maxn=0
maxcnt=0
for i in range(10):
    if li.count(i)>maxcnt:
        maxcnt=li.count(i)
        maxn=i

if maxn == 6 or maxn == 9:
    ans+=min(li.count(6),li.count(9))+(abs(li.count(6)-li.count(9))+1)//2
else:
    ans=maxcnt
print(ans)