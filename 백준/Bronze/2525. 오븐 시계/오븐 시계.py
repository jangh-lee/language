A, B = map(int, input().split())
C = int(input())
 
L = (B+C)/60
M = (B+C)%60
H = (L+A)%24
print(int(H), int(M))