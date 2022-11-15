"""
2022/10/01 22:05:01
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


N,M,K = IIS()
ABC = LLIIS(M)
E = LIIS()

dp = [INF] * (N+1)
dp[1] = 0
for e in E:
    a,b,c = ABC[e-1]
    dp[b] = min(dp[b], dp[a] + c)
print(dp[-1] if dp[-1] != INF else -1)