A,B=map(str,input().split())
Am=0
Bm=0
for i in range(0,len(A)):
    Am+=int(A[i])
for i in range(0,len(B)):
    Bm+=int(B[i])
print(Am*Bm)
