x1,y1= map(int, input().split())
x2,y2= map(int, input().split())
x3,y3= map(int, input().split())

#직선식 이용한 판별

if x1!=x2:
    if round((y2-y1)/(x2-x1)*(x3-x1)+y1,1)<y3:
        if x2>x1:
            print(1)
        elif x2<x1:
            print(-1)
        else:
            print(0)
    elif round((y2-y1)/(x2-x1)*(x3-x1)+y1,1)>y3:
        if x2>x1:
            print(-1)
        elif x2<x1:
            print(1)
        else:
            print(0)
    else:
        print(0)
else:
    if y1 > y2:
        if x3 > x1:
            print(1)
        elif x3 < x1:
            print(-1)
        else:
            print(0)
    elif y1 < y2:
        if x3 > x1:
            print(-1)
        elif x3 < x1:
            print(1)
        else:
            print(0)
    else:
        print(0)