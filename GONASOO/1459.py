X, Y, W, S = map(int, input().split())

x = max(X, Y)
y = min(X, Y)
sub = x-y

if S < 2*W:
    d = y*S
    if S < W:
        d += W*(sub%2) + S*(sub-(sub%2))
    else:
        d += sub*W

else:
    d = (x+y)*W

print(d)
