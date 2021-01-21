from operator import itemgetter

n = int(input())

r = 0
k = []

for i in range(n):
    tmp = list(map(int, input().split()))
    k.append(tmp)

for i in k:
    if k[:][0].count(i[0]) >= 2:
        r += 1
    if k[:][1].count(i[1]) >= 2:
        r += 1

print(r)

# nx = []
# ny = []
# k.sort(key=itemgetter(0))
# for i in range(len(k)):
#     for j in k[i+1:]:
#         if k[i][0] == j[0]:
#             if not k[i][0] in nx:
#                 nx.append(k[i][0])
#             break
#
# k.sort(key=itemgetter(1))
# for i in range(len(k)):
#     for j in k[i+1:]:
#         if k[i][1] == j[1]:
#             if not k[i][1] in ny:
#                 ny.append(k[i][1])
#             break
#
#print(len(nx)+len(ny))