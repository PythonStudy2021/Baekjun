num=int(input())
ans = 1
rat = 0
la = 1
while num>la:
    ans+=1
    rat+=6
    la+=rat
print(ans)