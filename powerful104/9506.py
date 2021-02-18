while True:
    num=int(input())
    if num==-1:
        break
    a=0
    li=[]
    for i in range(1,num):
        if num%i==0:
            a+=i
            li.append(i)
    if a==num:
        print("%d = " %num,end="")
        print(" + ".join(list(map(str,li))))
    else:
        print("%d is NOT perfect." %num)