def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
def LI(n): return [I() for _ in range(n)]
def PLUS(x,y): return [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]
def YES(): print('Yes'), exit()
def NO(): print('No'), exit()
import sys
sys.setrecursionlimit(500000)
INF = 10**10


N = II()
A = LIIS()
ALL = 60
MOD = 10**9+7

# 各bit毎に計算

ans = 0
for n in range(ALL):
    zero = 0
    one = 0
    t = 2 ** n
    for a in A:
        if a & t:
            one += 1
        else:
            zero += 1
    # 計算結果に影響があるのはXORなのでzeroとoneが組み合わさった時だけ
    ans += one * zero * (t % MOD)
    ans %= MOD
print(ans)