H, M = map(int, input().split())

rH, rM = 0, 0
if M >= 45:
    rH = H
    rM = M - 45
else:
    if H == 0:
        rH = 23
    else:
        rH = H - 1
    rM = M + 15

print(rH, rM)