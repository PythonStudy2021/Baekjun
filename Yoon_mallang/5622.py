word = list(input())
time = 0
for i in range(len(word)):
    if word[i] < chr(68):
        time += 3
    elif word[i] < chr(71):
        time += 4
    elif word[i] < chr(74):
        time += 5
    elif word[i] < chr(77):
        time += 6
    elif word[i] < chr(80):
        time += 7
    elif word[i] < chr(84):
        time += 8
    elif word[i] < chr(87):
        time += 9
    else:
        time += 10


print(time)