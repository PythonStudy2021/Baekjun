def bc(num, base):
    li=[]
    while num != 0:
        li.append(num % base)
        num = num // base
    li.reverse()
    return li

for i in range(1000,10000):
    if sum(list(map(int,list(str(i)))))==sum(bc(i,12))==sum(bc(i,16)):
        print(i)