a,b,c= map(int, input().split())
t=1
while True:
    if a-1==t%15 and b-1==t%28 and c-1==t%19:
        break
    t+=1
if(t==7980):
    print(1)
else:
    print(t+1)