S = input()
r = []
for i in range(len(S)):
    r.append(S[i:])
r.sort()
for i in r: print(i)
