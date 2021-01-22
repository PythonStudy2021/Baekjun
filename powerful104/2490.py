for _ in range(3):
    li = list(map(int, input().split()))
    cnt=li.count(0)
    if cnt==0:
        print("E")
    else:
        print(chr(64+cnt))