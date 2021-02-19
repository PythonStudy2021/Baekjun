int(input())
s=input()
ac=s.count("A")
bc=s.count("B")
if ac>bc:
    print("A")
elif ac<bc:
    print("B")
else:
    print("Tie")