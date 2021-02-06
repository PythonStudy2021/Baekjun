s=1
for _ in range(3):
    s*=int(input())
for i in range(10):
    print(str(s).count(str(i)))