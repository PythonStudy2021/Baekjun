A = [list(range(1,15))] + [[0]*14 for _ in range(14)]
for i in range(1,15):
    for j in range(14):
        A[i][j] = sum(A[i-1][:j+1])

T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    print(A[k][n-1])

