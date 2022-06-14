# 리스트 변수 a를 할당
a=[]

# 반복문을 통해서 append를 통해 인덱스 값을 주입함.
for i in range(9):
    a.append(int(input()))

# 최대값을 찾고, 그 값에 대한 인덱스를 표시하는데, 0부터 시작하기 때문에 '+1'로 인덱스 값 추가
print(max(a))
print(a.index(max(a))+1)