N = input()
for i in range(int(N)):
    if int(N) == i + sum(map(int,str(i))):
        print(i)
        exit()
print(0)