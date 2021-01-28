N = int(input())
list_N = []
black = N * 100
for i in range(N):
    A, B = map(int, input().split())
    list_N.append([A, B])
for i in range(N):
    for j in range(i+1, N):
        diff_X = list_N[i][0] - list_N[j][0]
        diff_Y = list_N[i][1] - list_N[j][1]
        if abs(diff_X) < 10 and abs(diff_Y) < 10:
            black -= (10 - abs(diff_X)) * (10 - abs(diff_Y))
print(black)