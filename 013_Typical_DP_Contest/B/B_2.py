"""
2022/09/25 0:13:09
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


a,b = IIS()
A = list(reversed(LIIS()))
B = list(reversed(LIIS()))

dp = [[-INF] * (b+1) for _ in range(a+1)]
# dp[aの山の残数][bの山の残数] = この山を担当したプレイヤーの点数差
dp[0][0] = 0
for i in range(a+1):
    for j in range(b+1):
        if not (i or j):
            continue
        if not j:
            # Aの山が残っていない
            dp[i][j] = max(dp[i][j], A[i-1] - dp[i-1][j])   # A点得る代わりに dp[i-1][j]の点数を取られてしまう
        elif not i:
            dp[i][j] = max(dp[i][j], B[j - 1] - dp[i][j-1])  # B点得る代わりに dp[i][j-1]の点数を取られてしまう
        else:
            dp[i][j] = max(dp[i][j], A[i-1] - dp[i-1][j], B[j - 1] - dp[i][j-1])

print((sum(A)+sum(B)+dp[-1][-1])//2)