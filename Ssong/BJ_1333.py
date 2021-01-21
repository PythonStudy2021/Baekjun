N, L, D = map(int, input().split())
flag = 0
total_len = 0
temp = D
while N:
    N -= 1
    total_len += L
    if total_len > D:
        while total_len > D:
            D += temp
        if total_len == D:
            print(D)
            flag = 1
            break
    if N != 0:
        total_len += 5
        if total_len > D:
            print(D)
            flag = 1
            break
if flag != 1:
    print(D)