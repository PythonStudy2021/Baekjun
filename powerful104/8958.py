num = int(input())
for _ in range(num):
    s = str(input())
    n=0
    total=0
    for i in s:
        if i=="O":
            n+=1
            total+=n
        else:
            n=0
    print(total)