def prime(num):
    for i in range(2,num//2+1):
        if num%i == 0:
            return 0
    return 1

N = int(input())
A = list(map(int, input().split()))
ans=0
for i in A:
    if i>1:
        ans += prime(i)
print(ans)