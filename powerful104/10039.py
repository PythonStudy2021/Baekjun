ans=0
for _ in range(5):
    num=int(input())
    if num<40:
        num=40
    ans+=num
print(ans//5)