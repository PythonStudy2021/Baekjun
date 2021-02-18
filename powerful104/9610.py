li=[0]*5
for _ in range(int(input())):
    a, b = map(int, input().split())
    if a==0 or b==0:
        li[4]+=1
    elif a>0:
        if b>0:
            li[0]+=1
        elif b<0:
            li[3]+=1
    elif a<0:
        if b>0:
            li[1]+=1
        elif b<0:
            li[2]+=1
for i in range(4):
    print("Q%d: %d" %(i+1,li[i]))
print("AXIS: %d" %li[4])