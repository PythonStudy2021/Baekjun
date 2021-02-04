n = input()
n_ = len(n)

if int(n)<=18:
    range_ = int(n)-1
    x = 1
else:
    x = int(n) - n_*9
    range_ = n_*9

for i in range(range_):
    iList = list(str(i+x))
    total = i+x
    for j in range(len(iList)):
        total += int(iList[j])
    if total == int(n):
        print(i+x)
        exit()
print(0)