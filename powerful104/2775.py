li = [[0 for col in range(14)] for row in range(15)]
for i in range(1,15):
    li[0][i-1]=i
    li[i-1][0]=1
li[14][0]=1
for i in range(1,15):
    for j in range(1,14):
        li[i][j]=li[i-1][j]+li[i][j-1]
num = int(input())
for _ in range(num):
    k=int(input())
    n=int(input())
    print(li[k][n-1])