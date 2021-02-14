num=int(input())
if num!=1:
    s=0
    a=0
    while num>s:
        a+=1
        s+=a
        if s>num:
            a-=1
    print(a)
else:
    print(1)