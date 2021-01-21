list=[]
sum=0
a=b=0
for _ in range(0,9):
    num=int(input())
    list.append(num)
    sum+=num
for i in range(0,8):
    for j in range(i+1,9):
        if(list[i]+list[j]==sum-100):
            a=i
            b=j
del list[b]
del list[a]
list.sort()
for i in range(0,7):
    print(list[i])