a,b= map(int, input().split())
b=b-45
check=0
if b<0:
    check=1
    b=60+b
if check==1:
    a=a-1
    if a<0:
        a=24+a
print(a,b)