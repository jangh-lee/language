year = int(input())

if year % 4 == 0:
    if year % 100 !=0 or year % 400==0:
      print("1")
    else:
      print("0")
else:
  print("0")

# 배운점 1. 중첩 if 문의 사용
# 배운점 2. if 조건에 or,and 사용시 대문자 불가능 및 띄어쓰기 준수
