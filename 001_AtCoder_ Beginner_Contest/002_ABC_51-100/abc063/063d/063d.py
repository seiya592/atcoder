"""
2022/09/20 16:10:00
"""
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
def CEIL(x,y): return -(-x // y)    # 除算を小数点切り上げ
import sys
sys.setrecursionlimit(500000)
INF = 10**17


N, A, B = IIS()
H = []
for _ in range(N):
    H.append(II())

ok = 10 ** 9 + 1
ng = 0

def calc(m):
    cnt = m     # 魔法が打てる回数

    AOE = (m*B) # 範囲攻撃で全体が受けているダメージ

    for h in H:
        if h - AOE >= 1:
            cnt -= CEIL((h - AOE), (A-B))
    return True if cnt >= 0 else False

while abs(ok-ng) > 1:
    mid = (ok+ng) // 2
    if calc(mid):
        ok = mid
    else:
        ng = mid
print(ok)