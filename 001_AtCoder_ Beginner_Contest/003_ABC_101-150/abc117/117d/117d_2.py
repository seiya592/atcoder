"""
2022/08/07 19:28:44
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
import sys
sys.setrecursionlimit(500000)
INF = 10**10


N, K = IIS()
A = LIIS()
ALL = 60
dp = [[-INF] * 2 for _ in range(ALL+2)]
#dp[上位n桁まで確定][K未満かフラグ] = 最大値
dp[0][0] = 0
for n in range(ALL+1):
    one = 0
    zero = 0
    for a in A:
        if a & (1 << (ALL-n)):
            one += 1
        else:
            zero += 1

    for k in range(2):
        if dp[n][k] < 0:
            continue

        dp[n+1][k|(K & (1 << (ALL-n))) != 0] = max(dp[n+1][k|(K & (1 << (ALL-n))) != 0], dp[n][k] + one * (1 << (ALL-n)))

        if k or K & (1 << (ALL- n)):
            dp[n+1][k] = max(dp[n+1][k], dp[n][k] + max(zero,one) * (1 << (ALL - n)))

        # if not k:
        #     if (K & 1 << (ALL-n)):
        #         dp[n+1][1] = dp[n][k] + one * (1 << (ALL-n))
        #     dp[n+1][k] = max(dp[n+1][k], dp[n][k] + one * (1 << (ALL-n)))
        # else:
        #     dp[n+1][k] = max(dp[n+1][k], dp[n][k] + max(zero,one) * (1 << (ALL - n)))
print(max(dp[-1]))


        # dp[n+1][k|(K)] = max(dp[n+1][k], dp[n][k] + (max(zero, one) if k else one) * (1 << (ALL - n)) )