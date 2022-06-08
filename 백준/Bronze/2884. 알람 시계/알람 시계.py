h,m = map(int, input().split())
l = m - 45 

if l <0:   # 45분을 뺄 때 음수 값이 나오면 문제가 생기므로 음수를 판별하고
    if h == 0:    # 혹 h값이 0일 경우 23이 나와야 하기 때문에 
      print(23, 60 + l)
    else:
      print(h-1, 60 + l)
else:
  print(h, l)




----
# https://ooyoung.tistory.com/28에서 가져온 영지공지님 코드가 더 깔끔하여 작성
 

H, M = map(int, input().split())

if M < 45 :	# 분단위가 45분보다 작을 때 
    if H == 0 :	# 0 시이면
        H = 23
        M += 60
    else :	# 0시가 아니면 (0시보다 크면)
        H -= 1	
        M += 60
        
print(H, M-45)	
