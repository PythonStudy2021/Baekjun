import random
num=0
h=[]
temp=[]
for i in range(0,9):
    num=int(input())
    h.append(num)
while True:
    temp=random.sample(h,7)
    if sum(temp)==100:
        temp.sort()
        print(temp)
        break
#solving
