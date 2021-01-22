lia=[]
lib=[]
lic=[]
for _ in range(4):
    lia.append(list("WBWBWBWB"))
    lia.append(list("BWBWBWBW"))
    lib.append(list("BWBWBWBW"))
    lib.append(list("WBWBWBWB"))
a,b= map(int, input().split())
for _ in range(a):
    lic.append(list(input()))
ansa=0
ansb=0
mina=65
minb=65
for i in range(a-7):
    for j in range(b-7):
        ansa = 0
        ansb = 0
        for k in range(8):
            for l in range(8):
                if lia[k][l]!=lic[i+k][j+l]:
                    ansa+=1
                if lib[k][l]!=lic[i+k][j+l]:
                    ansb+=1
        if ansa<mina:
            mina=ansa
        if ansb<minb:
            minb=ansb
print(min(mina,minb))