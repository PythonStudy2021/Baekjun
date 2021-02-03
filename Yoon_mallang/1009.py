t = int(input())
i = 0
x = []
p = [[10], [1], [2, 4, 8, 6], [3, 9, 7, 1], [4, 6], [5], [6], [7, 9, 3, 1], [8, 4, 2, 6], [9, 1]]

while i < t:
    a, b = map(int, input().split())
    x.append([a, b])
    i += 1
i = 0

while i < t:
    # print(p[x[i][0] % 10][x[i][1] % p[x[i][0] % 10][0]])
    a_ = x[i][0] % 10
    b_ = x[i][1] % len(p[a_])
    print(p[a_][b_-1])




    i += 1
