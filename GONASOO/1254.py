S = input(); s = len(S)

for i in range(s):
    if S[i:] == S[i:][::-1]:
        print(s+i)
        break
