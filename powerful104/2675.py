num = int(input())
for _ in range(num):
    li=""
    n, s = map(str, input().split())
    for i in list(s):
        i = i*int(n)
        li+=i
    print(li)