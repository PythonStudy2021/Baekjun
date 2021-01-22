import sys
num = int(input())
li=[]
for _ in range(num):
    li.append(int(sys.stdin.readline()))
li.sort()
ans=[]
for i in range(num):
    ans.append(li[i]*(num-(i)))
print(max(ans))