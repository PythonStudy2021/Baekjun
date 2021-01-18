n = int(input())
temp = n
a = []
count = 0
key = 0
while n:
    n -= 1
    tmp_x, tmp_y = map(int, input().split())
    a.append([tmp_x, tmp_y])
a.sort(key=lambda x: x[0])
i = 0
while i < temp - 1:
    for j in range(i + 1, temp):
        if key == a[i][0]:
            i += 1
            break
        if a[i][0] == a[j][0]:
            key = a[i][0]
            count += 1
            i += 1
        else:
            i = j
            break
a.sort(key=lambda x: x[1])
i = 0
while i < temp - 1:
    for j in range(i + 1, temp):
        if key == a[i][1]:
            i += 1
            break
        if a[i][1] == a[j][1]:
            key = a[i][1]
            count += 1
            i += 1
        else:
            i = j
            break
print(count + 1)