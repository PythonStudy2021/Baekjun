import math
num = []
a, b = map(int, input().split())
sum = 0
j = 1
k = 1
for i in range(b):
    if a <= i + 1 <= b:
        sum += k
    if j == k:
        j = 0
        k +=1
    j +=1
print(sum)