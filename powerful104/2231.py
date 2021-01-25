num = int(input())
ans=0
for i in range(1,num+1):
    su=0
    su = sum(map(int,list(str(i))))
    if i+su==num:
        ans=i
        break
print(ans)