num = int(input())
ans=0
for i in range(num-len(str(num))*9,num+1):
    if i>0:
        su=0
        su = sum(map(int,list(str(i))))
        if i+su==num:
            ans=i
            break
print(ans)