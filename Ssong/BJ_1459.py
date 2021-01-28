X, Y, W, S = map(int, input().split())
time = 0
diff = X - Y
if (2 * W) > S:
    if X < Y:
        diff = -diff
        time += (X * S)
        time += (diff * W)
    else:
        time += (Y * S)
        time += (diff * W)
else:
    time += (X * W)
    time += (Y * W)
print(time)