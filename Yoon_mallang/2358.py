ndot = int(input())
dots = []
line = 0
for i in range(ndot):
    x, y = map(int, input().split())
    dots.append([x, y])

Counter

for i in range(ndot-1):
    for j in range(i+1, ndot):
        if dots[i][0] == dots[j][0] and dots[i][1] == dots[j][1]:
            line += 2
        elif dots[i][0] == dots[j][0] or dots[i][1] == dots[j][1]:
            line += 1

print(line)