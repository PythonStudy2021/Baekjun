num = int(input())
li = list(map(int, input().split()))
ans = []
for i in range(num,0,-1):
    ans = ans[:li[i-1]]+[i]+ans[li[i-1]:]
print(" ".join(map(str,ans)))