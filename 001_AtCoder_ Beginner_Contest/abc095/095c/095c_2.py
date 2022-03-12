import sys

A, B, C, X, Y = map(int, input().split())
loop = max(X, Y)
price = sys.maxsize
tmp = 0
for i in range(loop + 1):
    tmp = ((A * max(X - i, 0)) + (B * max(Y - i, 0))) + (C * i * 2)
    if price > tmp:
        price = tmp
print(price)
