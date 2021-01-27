D = list(input())
W = list(input())
ct = r = 0
while ct <= len(D)-len(W):
    if D[ct:ct+len(W)] == W:
        r += 1
        ct += len(W)
    else: ct += 1
print(r)
