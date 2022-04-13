def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(10000000)


N = II()
A = LIIS()

total = sum(A)
if total % N != 0:
    print(-1)
    exit()
p = total // N
if p == 0:
    print(0)
    exit()

ans = 0
b = 0   # 掛けている橋
t = 0   # 繋がっている橋の合計
for a in A:
    t += a
    b += 1
    if t // p == b and t % p == 0:
        ans += b-1
        b = 0
        t = 0
else:
    if t != 0:
        print(-1)
        exit()
print(ans)