a, b = map(int, input().split())
aIndex = int(input())
aList = list(map(int,input().split())) 
z = []
num = 0
for i in range(aIndex):
    num += aList[i]*(a**(aIndex-i-1))

while True:
    if num>=b:
        x = num/b
        y = num%b
        z.append(y)
        num = num//b
    else:
        z.append(num)
        break

z.reverse()
for i in range(len(z)):
    print(z[i], end=" ")
    