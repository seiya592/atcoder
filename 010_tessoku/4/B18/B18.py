"""
2022/10/17 19:35:13
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
A = LIIS()

dp = [[0] * ((10000+1)*2) for _ in range(N+1)]
dp[0][0] = 1

# 配る
for n in range(N):
    for i in range(S+1):
        dp[n+1][i] += dp[n][i]
        dp[n+1][i+A[n]] += dp[n][i]

#ないばあい
if not dp[N][S]:
    print(-1)
    exit()

#復元
ans = []
now = S
for n in range(N-1,-1,-1):
    if now - A[n] >= 0 and dp[n][now-A[n]]:
        now -= A[n]
        ans.append(n+1)

print(len(ans))
print(*reversed(ans))