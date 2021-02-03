#시발 모르겠다
honest = 0
aryX = []
aryY = []
answer = 0
while True:
    x = int(input())
    if x == 0:
        exit()
    y = input()
    if y == "right on":
        answer = x
        for i in range(len(aryX)+1):
            if honest == 0 and i == len(aryX):
                print("Stan may be honest")
                aryX = []
                aryY = []
                answer = 0
                break
            if honest == 0 and aryX[i] >= answer and aryY[i] == "too low":
                print("Stan is dishonest")
                honest = 0
                aryX = []
                aryY = []
                answer = 0
                break
            elif honest == 0 and aryX[i] <= answer and aryY[i] == "too high":
                print("Stan is dishonest")
                honest = 0
                aryX = []
                aryY = []
                answer = 0
                break
            i += 1
    else:
        aryX.append(x)
        aryY.append(y)
