def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))


A, B, C, X = LIIS()

if X <= A:
    print("1.00000000000")
elif B < X:
    print("0.0000000")
else:
    print(C / (B - A))
