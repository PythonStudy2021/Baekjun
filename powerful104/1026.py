num = int(input())
lia = list(map(int, input().split()))
lib = list(map(int, input().split()))
lia.sort()
lib.sort(reverse=True)
lic = [lia[i]*lib[i] for i in range(num)]
print(sum(lic))