list_N = []
list_S = []
max_n = 10
min_n = 1
while True:
    N = int(input())
    if N == 0:
        break
    S = input()
    list_N.append(N)
    list_S.append(S)
    if S == 'too high':
        max_n = N
    elif S == 'too low':
        min_n = N
    elif S == 'right on':
        if N <= min_n or N >= max_n:
            print('Stan is dishonest')
        else:
            print('Stan may be honest')