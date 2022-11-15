"""
2022/10/18 17:34:39
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


S = I()
T = I()
S_s = len(S)
T_s = len(T)

dp = [[INF] * (T_s+1) for _ in range(S_s+1)]
dp[0][0] = 0
for i in range(S_s+1):
    for j in range(T_s+1):
        if i == j == 0:
            continue
        if i == 0:
            dp[i][j] = dp[i][j-1] + 1
            continue
        if j == 0:
            dp[i][j] = dp[i-1][j] + 1
            continue

        if S[i-1] == T[j-1]:
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j] + 1, dp[i][j-1]+1)
        else:
            dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1]+1, dp[i-1][j-1]+1)
print(dp[-1][-1])