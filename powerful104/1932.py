num = int(input())
li=[]
for _ in range(num):
    li.append(list(map(int, input().split())))
for i in range(1,num):
    for j in range(i+1):
        if j==i:
            li[i][j]+=li[i-1][j-1]
        elif j==0:
            li[i][j]+=li[i-1][j]
        else:
            li[i][j]+=max(li[i-1][j-1],li[i-1][j])
print(max(li[num-1]))