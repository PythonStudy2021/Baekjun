num = int(input())
c=""
if num>59:
    c=chr(74-num//10)
    if c=="@":
        c="A"
else:
    c="F"
print(c)