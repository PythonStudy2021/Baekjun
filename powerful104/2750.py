import sys
num = int(input())
li=[]
for _ in range(num):
    li.append(int(sys.stdin.readline()))
li.sort()
for i in li:
    print(i)