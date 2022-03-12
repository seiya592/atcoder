def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))

N = II()
A = LIIS()
debug = []
P = [False] * 360
tmp = 0
P[0] = True
for a in A:
    tmp += a
    P[tmp % 360] = True

# 確認
ans = 0
tmp = 1
for i in range(360):
    if P[i]:
        ans = max(ans, tmp)
        tmp = 1
    else:
        tmp += 1
else:
    ans = max(ans, tmp % 360)

print(ans)