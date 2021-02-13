K = input()

c = r = 0
for i in range(len(K)):
    if K[i] == '(':
        c += 1
    else:
        c -= 1
        if K[i-1] == '(': r += c
        else: r += 1
print(r)
