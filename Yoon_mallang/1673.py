try:
    while True:
        n, k = map(int, input().split())

        # if k <= 1 or n < k:
        #     break

        chicken = n
        n_ = n

        while True:
            if k <= 1 or n < k:
                print(0)
                break

            chicken = chicken + int(n_ / k)
            n_ = int(n_ / k) + int(n_ % k)
            if n_ < k:
                print(chicken)
                break

except EOFError:
    exit()
