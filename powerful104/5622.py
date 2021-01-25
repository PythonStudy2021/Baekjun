ans = 0
s = input()
for i in list(s):
    c=ord(i)
    if c<80:
        ans+=(c-65)//3+3
    elif c<84:
        ans+=8
    elif c<87:
        ans+=9
    elif c<91:
        ans+=10
print(ans)