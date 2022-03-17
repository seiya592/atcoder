A, B, C, X, Y = map(int, input().split())
price = 0
if A + B <= C * 2:
    price = (A * X) + (B * Y)
else:
    if Y > X:
        price = C * X * 2
        if B > C * 2:
            price += C * 2 * (Y - X)
        else:
            price += B * (Y - X)
    else:
        price = C * Y * 2
        if A > C * 2:
            price += C * 2 * (X - Y)
        else:
            price += A * (X - Y)
print(price)

# Cbuy = min(X, Y)
# price = Cbuy * 2 * C
# X -= Cbuy
# Y -= Cbuy
# price += (A * X) + (B * Y)
