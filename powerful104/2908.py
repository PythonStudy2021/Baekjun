a,b= map(str, input().split())
lia = list(a)
lib = list(b)
lia.reverse()
lib.reverse()
print(max(int("".join(lia)),int("".join(lib))))