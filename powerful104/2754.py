import sys
input = sys.stdin.readline
c=input().strip()
score=0.0
if c[0]=="A":
    score+=4.0
elif c[0] == "B":
    score+=3.0
elif c[0] == "C":
    score+=2.0
elif c[0] == "D":
    score+=1.0
if c[0]!="F":
    if c[1]=="+":
        score+=0.3
    elif c[1]=="-":
        score-=0.3
print(score)