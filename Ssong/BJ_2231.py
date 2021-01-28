N = int(input())
flag = 0
for i in range(1, N):
    tmp = str(i)
    total = 0
    for j in tmp:
        total += int(j)
    if N == (i + total):
        print(i)
        flag = 1
        break
if flag == 0:
    print(0)