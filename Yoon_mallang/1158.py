n, k = map(int, input().split())
people = []
ary = []
count = 1

#a = list(range(1,n+1)) 밑에 for 안쓰고 이렇게 할 수 있음 
for i in range(n):
    people.append(str(i+1))

i = 0
while len(people) > 0:
    i = (i + k - 1) % len(people)
    ary.append(people[i])
    del people[i]

#사이사이 마다 원하는 string 넣어주는게 join 인듯 
print("<%s>" %(", ".join(ary)))

#join 뭔지 공부, 애들꺼보고 학습 