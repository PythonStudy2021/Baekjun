n = int(input())
num = 665
nCount = 0

while True:
    if '666' in str(num):
        nCount +=1
        if nCount == n:
            print(num)
            break
    num+=1


# 참 못짠 똥 코드 
# n = int(input())
# num = "665"
# count = 0
# nCount = 0
# while True:
#     numList = list(num)
#     for i in range(len(numList)):
#         if numList[i] == '6':
#             count += 1
#         else:
#             count = 0
#         if count == 3:
#             count = 0
#             nCount +=1
#             break
#     count = 0
#     if nCount == n:
#         print(num)
#         break
#     else:
#         num = int(num)
#         num+=1
#         num = str(num)

