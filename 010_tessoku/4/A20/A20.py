"""
2022/10/18 17:25:46
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
dp = [[0] * (T_s+1) for _ in range(S_s+1)]

for i in range(1,S_s+1):
    for j in range(1,T_s+1):
        if S[i-1] == T[j-1]:
            dp[i][j] = max(dp[i-1][j-1]+1, dp[i-1][j], dp[i][j-1])
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
print(dp[-1][-1])