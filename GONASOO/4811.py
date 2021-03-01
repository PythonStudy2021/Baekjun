def factorial(x):
    for i in range(2, x):
        x *= i
    return x


while True:
    N = int(input())
    if not N: break
    print(factorial(N * 2) // ((factorial(N) ** 2) * (N + 1)))
