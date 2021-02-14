a,b,c = map(int, input().split())
d = int(input())
sec=(a*3600+b*60+c+d)%86400
print(sec//3600,sec%3600//60,sec%60)