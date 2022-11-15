"""
2022/10/01 20:39:15
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


N,S = IIS()
AB = LLIIS(N)
dp = [[0] * (S+1) for _ in range(N+1)]
dp[0][0] = 1

for n in range(N):
    a,b = AB[n]
    for s in range(S+1):
        # dp[n + 1][s] += dp[n][s]
        if s+a<= S:
            dp[n+1][s+a] += dp[n][s]
        if s+b <= S:
            dp[n+1][s+b] += dp[n][s]


if not dp[-1][-1]:
    NO()

now = S
ans = ''
for n in range(N,0,-1):
    a,b = AB[n-1]
    if dp[n-1][S-a]:
        ans = 'H' + ans
        S -= a
    else:
        ans = 'T' + ans
        S -= b
print('Yes')
print(ans)