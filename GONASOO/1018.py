N, M = map(int, input().split())

C = []
for _ in range(N): C.append(list(input()))

ct = [0 for _ in range((N-7)*(M-7)*2)]
cct = 0

for i in range(N-7):
    for j in range(M-7):
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l)%2:
                    if C[k][l] == 'W': ct[cct] += 1
                    else: ct[cct+1] += 1
                else:
                    if C[k][l] == 'W': ct[cct+1] += 1
                    else: ct[cct] += 1

        cct += 2

print(min(ct))