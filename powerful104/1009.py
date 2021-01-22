num=int(input())
for i in range(num):
    a,b=map(int,input().split())
    c=(a%10)**(4+b%4)
    print(c%10+int(c%10==0)*10)