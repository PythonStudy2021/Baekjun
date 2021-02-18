map_ = [[0 for col in range(101)] for row in range(101)]
p_x=50
p_y=50
p_a=0
max_x=50
min_x=50
max_y=50
min_y=50
arrow=[0,1,2,3]
moving=[(0,-1),(-1,0),(0,1),(1,0)]
map_[p_y][p_x]=1
n=int(input())
for i in list(input().strip()):
    if i=="F":
        p_x+=moving[p_a][0]
        p_y+=moving[p_a][1]
        if p_x>max_x:
            max_x=p_x
        if p_x<min_x:
            min_x=p_x
        if p_y>max_y:
            max_y=p_y
        if p_y<min_y:
            min_y=p_y
        map_[p_y][p_x] = 1
    elif i=="L":
        p_a=arrow[p_a-1]
    elif i=="R":
        p_a=arrow[p_a-3]
for i in range(max_y,min_y-1,-1):
    for j in range(min_x,max_x+1):
        if map_[i][j]==1:
            print(".",end="")
        else:
            print("#",end="")
    print("")