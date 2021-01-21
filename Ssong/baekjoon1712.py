A, B, C = input().split()
A = float(A)
B = float(B)
C = float(C)
if (C-B) == 0:
    print(-1)
    exit()
gain = A / (C-B)
gain = int(gain)
if gain < 0:
    print(-1)
elif gain >= 0:
    print(gain+1)