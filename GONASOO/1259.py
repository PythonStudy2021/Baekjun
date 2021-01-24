while True:
    K = input()
    if K == '0': break
    if K[::-1] == K: r = "yes"
    else: r = "no"
    print(r)