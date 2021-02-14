# import time
#
# st = time.time()

N = int(input())

D = {1:0,2:1,3:1}
for i in range(4,N+1):
    a = D[i//3] + 1 if not i%3 else 9999999
    b = D[i//2] + 1 if not i%2 else 9999999
    c = D[i-1] + 1
    D[i] = min(a,b,c)
print(D[N])

# print(time.time()-st)