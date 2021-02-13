# import time
#
# st = time.time()

f = [0,1]
for i in range(2,41):
    f.append(f[i-1] + f[i-2])

for _ in range(int(input())):
    k = int(input())
    if k == 0: print(1,0)
    else: print(f[k-1],f[k])

# print(time.time() - st)