lix=set()
liy=set()
for _ in range(3):
    a, b = map(int, input().split())
    if a in lix:
        lix.remove(a)
    else:
        lix.add(a)
    if b in liy:
        liy.remove(b)
    else:
        liy.add(b)
print(list(lix)[0],list(liy)[0])