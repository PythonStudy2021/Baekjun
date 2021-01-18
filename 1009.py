T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    if a%10 == 0: r=10
    else: r=(int(pow(a%10, b%4+4)))%10
    print(r)