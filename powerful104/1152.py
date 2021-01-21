a = input(str())#a입력받음
com = 0 #단어개수 저장할 com초기화
a.strip()#입력받은 a를 양옆의 공백을 제거
com += len(a.split())#a를 나누고 나눈 단어의 개수를 세주어서 com 에다 더함
print(com)#com 출력