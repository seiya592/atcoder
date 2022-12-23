"""
2022/12/10 19:10:59
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
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(500000)
INF = 10**17


N,M = IIS()
W = LIIS()
C = LIIS()
WC = [(w,c) for w,c in zip(W,C)]
WC.sort(key=lambda x:x[1])
ColorNum = len(set(C))

dp = [[0] * (M+1) for _ in range(ColorNum+1)]
dp[0][0] = 1

c = 1
now = WC[0][1]
n = 0
while c < ColorNum+1:

    for w in range(M+1):
        # 選ばない
        dp[c][w] += dp[c-1][w]

        # 選ぶ
        if w-WC[n][0] >= 0:
            dp[c][w] += dp[c-1][w-WC[n][0]]

    n += 1
    if n >= N:
        break

    if WC[n][1] != now:
        c += 1
        now = WC[n][1]

for i in range(1,ColorNum+1):
    if dp[i][M]:
        YES()
NO()