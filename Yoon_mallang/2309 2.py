import random
n = 0
total=0
nan = []
while n < 9:
    x = int(input())
    nan.append(x)
    total = total + nan[n]
    n += 1


i = 0
nNan = []
nTotal = 0
tNum = 8
nan.sort()

if total-nan[0]-nan[1] > 100:
    for i in range(7):
        print(nan[i])
else:
    while True:
        if tNum > 0:
            ranNum = random.randint(0, tNum)

        nNan.append(nan[ranNum])
        nan.pop(ranNum)
        nTotal += nNan[i]
        tNum -= 1
        i += 1
        if tNum < 2:
            for i in range(7):
                nNan.sort()
                print(nNan[i])
            break

