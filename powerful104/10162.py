num=int(input())
if num%10!=0:
    print("-1")
else:
    print("%d %d %d" %(num//300,num%300//60,num%60//10))