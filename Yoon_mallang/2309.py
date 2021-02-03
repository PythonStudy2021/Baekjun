import random
n = 0
total = 0
nan = []
oNan = []
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
oNan = nan.copy()
while True:
    ranNum = random.randint(0, tNum)
    nNan.append(oNan[ranNum])
    oNan.pop(ranNum)
    nTotal += nNan[i]
    tNum -= 1
    i += 1
    if tNum < 2 and nTotal == 100:
        for i in range(7):
            nNan.sort()
            print(nNan[i])
        break
    elif tNum < 2:
        nTotal = 0
        nNan = []
        tNum = 8
        oNan = nan.copy()
        i=0

# 깔끔한 송호준 코드
# import random
# num = []
# for i in range(9):
#     x = int(input())
#     num.append(x)
# while True:
#     tmp = random.sample(num, 7)
#     key = sum(tmp)
#     if key == 100:
#         tmp.sort()
#         for i in range(len(tmp)):
#             print(tmp[i])
#         break