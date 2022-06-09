n, x = map(int,input().split())
a = list(map(int,input().split()))
b = []

for i in range(0, n):
  if a[i] < x:
    b.append(a[i])

print(' '.join(str(x) for x in b))