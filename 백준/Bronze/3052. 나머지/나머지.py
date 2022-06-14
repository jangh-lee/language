# 10개의 수를 차례로 입력받는다
# 각 수는 입력받고 42로 나눠지며, 나머지 값을 구해야한다.
# 따라서, 입력받는 즉시 42로 나눈 나머지를 list에 저장하겠다.

# 나머지를 저장할 list 변수를 할당한다.
left = []

# 나누기 연산이므로, 정수값으로 변환해주면서 입력받는다.
for i in range(10):
  a = int(input())
  left.append(a%42)

# 나온 left 변수에 중복값을 제거한다.
# 방법1. list - set - list 변환
nosame = list(set(left))

# 방법2. for문을 통해 중복된 값은 이탈시킴

# 중복값이 제거된 총 길이가 갯수 값이므로 해당 값을 출력한다.
print(len(nosame))