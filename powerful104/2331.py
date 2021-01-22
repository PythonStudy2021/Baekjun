a,b= map(int, input().split())
li=[]
num=a
while True:
    li.append(num)
    s=list(str(num))
    num=0
    for i in s:
        num+=int(i)**b
    if num in li:
        break
li=li[:li.index(num)]
print(len(li))