sli=[]
li=[]
num=int(input())
for _ in range(num):
    sli.append(input().strip())
for i in range(len(sli[0])):
    check=0
    for j in range(num-1):
        if sli[j][i]!=sli[j+1][i]:
            check=1
            break
    if check==1:
        li.append(i)
ans=[]
for i in range(len(sli[0])):
    if i in li:
        ans.append("?")
    else:
        ans.append(sli[0][i])
print("".join(ans))