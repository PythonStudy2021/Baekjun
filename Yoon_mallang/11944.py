n, m = input().split()
m = int(m)
iN = int(n)
j = 0
nLen = len(n)

if iN * nLen > m:
    for i in range(m):
        print(n[j%nLen], end='')
        j += 1
else:
    for i in range(iN):
        print(n, end='')


# n,m=map(int,input().split())
# print((str(n)*n)[:m])
# 효율적인 강희 코드
