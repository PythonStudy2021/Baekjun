exBee = 0
bee = 1
count = 1
line = int(input())
i = 6

while True:
    if exBee <= line <= bee:
        print(count)
        break
    count += 1
    exBee = bee
    bee = bee + i
    i = i + 6

    # if count%2 != 0:
    #     i += 1
