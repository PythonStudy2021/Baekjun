def fibo(n):
    if n==0:
        return 0
    fn = 0
    fn1 = 1
    ans = fn1
    for _ in range(n - 1):
        ans = (fn + fn1)%1000000000
        fn = fn1%1000000000
        fn1 = ans
    return ans
num = int(input())
if num<0:
    if (num*(-1))%2==0:
        print(-1)
    else:
        print(1)
    num*=-1
elif num==0:
    print(0)
else:
    print(1)
print(fibo(num))