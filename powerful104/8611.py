def bc(num, b):
    lit=[]
    while num!=0:
        lit.append(num%b)
        num=num//b
    lit.reverse()
    return lit

def palin(s):
    ans = 1
    for i in range(len(s) // 2):
        if s[i] != s[-(1 + i)]:
            ans = 0
    return ans

num=int(input())
check=0
for i in range(2,11):
    li=bc(num,i)
    if palin(li)==1:
        print(i, "".join(map(str,li)))
        check=1
if check!=1:
    print("NIE")