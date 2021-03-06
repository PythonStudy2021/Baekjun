x = [0,0,0]; y = [0,0,0]
for i in range(3): x[i],y[i] = map(int,input().split())

a = (x[0]*y[1] + x[1]*y[2] + x[2]*y[0]) - (y[0]*x[1] + y[1]*x[2] + y[2]*x[0])

if a: r = a//abs(a)
else: r = 0
print(r)