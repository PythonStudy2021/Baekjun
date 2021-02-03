n = int(input())
hw = [list(map(int, input().split())) for _ in range(n)]
# 미친 대박
# print(hw)
rank = []
for i in range(n):
    rank.append(1)
    # for j in range(n):
    #     if hw[i][0] > hw[j][0] or hw[i][1] > hw[j][1]:
    #         rank[i] -= 1
    #     elif hw[i][0] == hw[j][0] and hw[i][1] == hw[j][1]:
    #         rank[i] -= 1
    for j in range(n):
        if hw[i][0] < hw[j][0] and hw[i][1] < hw[j][1]:
            rank[i] += 1

for i in range(n):
    print(rank[i], end=' ')
