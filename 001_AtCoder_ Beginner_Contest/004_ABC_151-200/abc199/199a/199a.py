# a,b,c,d = (map(int, input().split()))
# gridList = [list(map(int, input().split())) for i in range(N)]
import math

X,Y,Z = (map(int, input().split()))
print(math.ceil(Y/X * Z) - 1)

