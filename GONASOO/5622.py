S = input()
r = 0
for i in S:
    if 'A' <= i <= 'C': r += 3
    elif 'D' <= i <= 'F': r += 4
    elif 'G' <= i <= 'I': r += 5
    elif 'J' <= i <= 'L': r += 6
    elif 'M' <= i <= 'O': r += 7
    elif 'P' <= i <= 'S': r += 8
    elif 'T' <= i <= 'V': r += 9
    elif 'W' <= i <= 'Z': r += 10
    elif i == '1': r += 2
    else: r += 11
print(r)

