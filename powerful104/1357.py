li = list(map(list, map(str, input().split())))
li[0].reverse()
li[1].reverse()
num = list(str(int(''.join(li[0]))+int(''.join(li[1]))))
num.reverse()
print(int(''.join(num)))