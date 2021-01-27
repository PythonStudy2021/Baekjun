N,K=map(int,input().split())
a=[]
b=[]
for i in range(0,N):
    a.append(i+1)
temp=K
index=0
for i in range(0,N):
    index+=K
    b.append(a[index-1])
    del a[index-1]

