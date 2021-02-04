num=int(input())
li=[]
r=0
c=0
for _ in range(num):
    s=input().strip()
    sli=s.split("X")
    for i in range(len(sli)):
        if len(sli[i])>1:
            r+=1
    li.append(s)
newli = list(map(list,zip(*li)))
for i in range(num):
    sli = "".join(newli[i]).split("X")
    for j in range(len(sli)):
        if len(sli[j])>1:
            c+=1
print(r,c)