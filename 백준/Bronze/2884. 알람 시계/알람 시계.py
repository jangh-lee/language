h,m = map(int, input().split())
l = m - 45

if l <0:
    if h == 0:
      print(23, 60 + l)
    else:
      print(h-1, 60 + l)
else:
  print(h, l)