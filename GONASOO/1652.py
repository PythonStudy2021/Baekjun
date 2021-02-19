N = int(input()); S = []
for _ in range(N): S.append(list(input()))
x = y = 0

for i in range(N):
    a = 0
    for j in range(N):
        if S[i][j] == '.':
            a += 1
        else:
            if a > 1: x += 1
            a = 0
        if j == N-1 and a > 1:
            x += 1

for j in range(N):
    b = 0
    for i in range(N):
        if S[i][j] == '.':
            b += 1
        else:
            if b > 1: y += 1
            b = 0
        if i == N-1 and b > 1:
            y += 1

print(x,y)