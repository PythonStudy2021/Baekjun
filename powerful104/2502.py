def fibo(n):
    fn = 0
    fn1 = 1
    ans = fn1
    for _ in range(n - 1):
        ans = fn + fn1
        fn = fn1
        fn1 = ans
    return ans
d, k = map(int, input().split())
a = fibo(d-2)
b = fibo(d-1)
ansa=0
ansb=1
while True:
    ansa+=1
    if (k-ansa*a)%b==0:
        ansb=(k-ansa*a)//b
        break
print(ansa)
print(ansb)