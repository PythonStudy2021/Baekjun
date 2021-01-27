N = int(input())

C = []
for _ in range(N):
    X, Y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            if not [X+j, Y+i] in C:
                C.append([X+j, Y+i])

print(len(C))
