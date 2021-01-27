N = int(input())
M = list(map(int,input().split()))

pc = [0, 0] + [1 for _ in range(1000-1)] # [0,1]+[2,3,...,N]
r = 0
for i in range(2, 1000+1):
    if pc[i]:
        if i in M: r += 1
        for j in range(i*2,1000+1,i):
            pc[j] = 0

print(r)
