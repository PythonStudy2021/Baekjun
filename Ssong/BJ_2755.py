N = int(input())
a = []
total_point = 0
total_grade = 0
while N:
    N -= 1
    name, point, grade = input().split()
    if grade == 'A+':
        grade = 4.3
    elif grade == 'A0':
        grade = 4.0
    elif grade == 'A-':
        grade = 3.7
    elif grade == 'B+':
        grade = 3.3
    elif grade == 'B0':
        grade = 3.0
    elif grade == 'B-':
        grade = 2.7
    elif grade == 'C+':
        grade = 2.3
    elif grade == 'C0':
        grade = 2.0
    elif grade == 'C-':
        grade = 1.7
    elif grade == 'D+':
        grade = 1.3
    elif grade == 'D0':
        grade = 1.0
    elif grade == 'D-':
        grade = 0.7
    elif grade == 'F':
        grade = 0.0
    total_point += int(point)
    total_grade += (int(point) * grade)
total = total_grade / total_point
if int(total * 1000) % 10 == 5:
    total += 0.001
print('%.2f' % total)