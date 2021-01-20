import sys

def binary_search(target, data):
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return 1
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid -1

    return 0

N = int(input())
A = list(map(int, sys.stdin.readline().split()))
A.sort()
M = int(input())
B = list(map(int, sys.stdin.readline().split()))
for i in B:
    print(binary_search(i,A))