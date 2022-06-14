# 곱할 3 수를 입력받음
A= int(input())
B= int(input())
C= int(input())

# 3수의 곱에 대해서 분할을 위해 스트링으로 변환
multiple = str(A*B*C)

# 한글자씩 list에 담기
y = list(multiple)

# (참고)한글자씩 append를 통해서 list에 넣음
m = []
for i in multiple:
  m.append(i)

# print가 길어져서 반복문으로 해결
for num in range(10):
  print(y.count(str(num)))