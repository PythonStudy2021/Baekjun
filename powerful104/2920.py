a,b,c,d,e,f,g,h = map(int, input().split())
li=[1,2,3,4,5,6,7,8]
tmp=[a,b,c,d,e,f,g,h]
if tmp==li:
    print("ascending")
else:
    li.reverse()
    if tmp==li:
        print("descending")
    else:
        print("mixed")