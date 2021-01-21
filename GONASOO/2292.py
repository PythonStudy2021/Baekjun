N = int(input())

if N == 1:
    r = 1
elif N < 3:
    r = 2
else:
    i, j = 0, 0
    while True:
        if N-2 >= 6*i and N-2 < 6*(i+j+1):
            r = j + 2
            break
        else:
            j += 1
            i += j

print(r)
