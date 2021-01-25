li=[0]*100
lit=[]
for i in range(100):
    lit.append(list(li))
li=[]
num = int(input())
for i in range(num):
    a,b= map(int, input().split())
    li.append((a,b))
for i in li:
    for j in range(i[0]-1,i[0]-1+10):
        for k in range(i[1]-1,i[1]-1+10):
            lit[j][k]=1
ans = 0
for i in lit:
    ans += sum(i)
print(ans)