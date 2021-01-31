xy = []
for _ in range(int(input())):
    xy.append(list(map(int,input().split())))
for i in sorted(xy): print(i[0], i[1])