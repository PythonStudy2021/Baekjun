X, N = map(int, input().split())

if N == 0:
    if X > 0: print("INFINITE")
    else: print(0)
elif N == 1:
    if X < 0: print("INFINITE")
    else: print(0)
elif N % 2 == 1:
    print("ERROR")
else:
    if X > 0: print(int((X-1)//(N/2)))
    else: print(0)
