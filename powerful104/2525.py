hour=[i for i in range(0,24)]
a,b = map(int, input().split())
c = int(input())
print(hour[a-(24-(b+c)//60)],(b+c)%60)