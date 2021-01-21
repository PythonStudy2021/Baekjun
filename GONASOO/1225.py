A, B = input().split()
ra = 0
rb = 0

for i in A:
    ra += int(i)
for j in B:
    rb += int(j)

print(ra * rb)
