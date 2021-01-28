str = input()
count = 0
for i in str:
    if i >= 'A' and i < 'D':
        count += 3
    elif i >= 'D' and i < 'G':
        count += 4
    elif i >= 'G' and i < 'J':
        count += 5
    elif i >= 'J' and i < 'M':
        count += 6
    elif i >= 'M' and i < 'P':
        count += 7
    elif i >= 'P' and i < 'T':
        count += 8
    elif i >= 'T' and i < 'W':
        count += 9
    else:
        count += 10
print(count)