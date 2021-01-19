import random
array=[]
ret_array=[]
for i in range(0,9):
    b=int(input())
    array.append(b)
while True:
    sum = 0
    ret_array=random.sample(array,7)
    for i in range(0,7):
        sum += ret_array[i]
    if sum==100:
        break
    else:
        ret_array.clear()
        continue
ret_array.sort()
print(ret_array)

