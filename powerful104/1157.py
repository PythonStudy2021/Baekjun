s = input().upper()
d={}
for i in list(s):
    d.setdefault(i,0)
    d[i]+=1
li=[k for k,v in d.items() if max(d.values()) == v]
if len(li)==1:
    print(li[0])
else:
    print("?")