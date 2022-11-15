"""
2022/10/18 18:13:22
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


N = II()
S = I()

dp = [[0] * (N) for _ in range(N)]

# 初期値
for i in range(N):
    dp[i][i] = 1    # 同じ位置の文字は2固定
for i in range(N-1):
    dp[i][i+1] = 2 if S[i] == S[i+1] else 1     # 2つ並んだ文字が同じ場合は2文字でカウント（偶数）　この処理で偶奇を考えなくてよくなる

for length in range(2,N):    # 文字間の長さ
    for l in range(N-length):    # 左端
        r = l + length

        if S[l] == S[r]:
            dp[l][r] = max(dp[l+1][r], dp[l][r-1], dp[l+1][r-1] + 2)
        else:
            dp[l][r] = max(dp[l + 1][r], dp[l][r - 1])
print(dp[0][N-1])