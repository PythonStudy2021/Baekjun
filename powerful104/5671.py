li=[]
for i in range(1,5001):
    se=set(list(str(i)))
    if len(se) == len(str(i)):
        li.append(i)

while True:
    try:
        a, b = map(int, input().split())
        print(len(set(li)&set(list(range(a,b+1)))))
    except EOFError:
        break