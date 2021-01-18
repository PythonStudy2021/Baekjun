import random
num = []
for i in range(9):
    x = int(input())
    num.append(x)
while True:
    tmp = random.sample(num, 7)
    key = sum(tmp)
    if key == 100:
        tmp.sort()
        for i in range(len(tmp)):
            print(tmp[i])
        break