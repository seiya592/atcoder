"""
2022/11/14 20:25:01
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


N,K = IIS()
A = LIIS()
dp = [0] * (N+1+max(A))
# dp[残りの石がi個のターンを持ったプレイヤーは] = 0→負け 1→勝ち

for i in range(N):
    for a in A:
        dp[i+a] |= 1^dp[i]
print('First' if dp[N] else 'Second')