n=int(input())
spot=[n]
county=0
sum=0
for i in range(0,n):
    x,y=map(int,input().split())
    spot.append([x,y])
for i in range(0,n):
    county=spot[i][0]
    for j in range(i,n):
        if spot[i][0]==spot[j][0]:
            sum+=1
            #solving.
