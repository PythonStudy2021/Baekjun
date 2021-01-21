N = int(input())
n = N - 7
q = n // 19
m = n % 19

if N < 7:
    r = (N - 1) * (10 ** 3) + 666
else:
    if m < 10:
        r = int(str(q) + str(666) + str(m))
    else:
        r = int(str(m - 3 + 10 * q) + str(666))

print(r)

