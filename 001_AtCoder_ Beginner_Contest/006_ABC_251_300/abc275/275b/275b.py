"""
2022/10/29 20:51:57
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
MOD = 998244353

ABCDEF = LIIS()

#ABC
ABC = (ABCDEF[0] % MOD) * (ABCDEF[1] % MOD)
ABC %= MOD
ABC *= ABCDEF[2]
ABC %= MOD

DEF = (ABCDEF[3] % MOD) * (ABCDEF[4] % MOD)
DEF %= MOD
DEF *= ABCDEF[5]
DEF %= MOD

print(((ABC+MOD)-DEF)%MOD)