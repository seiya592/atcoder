"""
2022/10/21 19:10:10
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


N, M = IIS()
A = LLIIS(M)
Q = []
for a_ in A:
    now = 1
    s = 0
    for a in reversed(a_):
        s += now * a
        now *= 2
    Q.append(s)

ALL = 2 ** N
dp = [INF] * ALL
dp[0] = 0
for n in range(ALL):
    for q in Q:
        dp[n|q] = min(dp[n|q], dp[n] + 1)
print(dp[-1] if dp[-1] != INF else -1)