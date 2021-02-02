yx = []
for _ in range(int(input())):
    yx.append(list(reversed(list(map(int,input().split())))))
for i in sorted(yx): print(i[1], i[0])