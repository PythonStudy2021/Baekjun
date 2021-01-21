a,b= map(int, input().split())
num=a
li=[]
li.append(a)
while True:
    num = num*a%b
    if num in li:
        break
    li.append(num)
print(len(li)-li.index(num))