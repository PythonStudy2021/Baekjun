A, B = map(int, input().split())
list = []
count = 1
num = 1
while B:
    for i in range(num):
        if B == 0:
            break
        count = num
        list.append(count)
        B -= 1
    num += 1
sum = 0
for i in range(A - 1, len(list)):
    sum += list[i]
print(sum)