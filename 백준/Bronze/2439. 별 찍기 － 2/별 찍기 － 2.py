num = int(input())

for i in range(1, num+1):
    star = "*"*i
    print(star.rjust(num))
    
    
# print 문에서 str.rjust(num) 이 오른쪽 정렬 / ljust(num)이 왼쪽 정렬이다.
