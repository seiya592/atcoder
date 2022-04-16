def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(10000000)


N = II()
H = LIIS()

# 配るDP
dp = [10**10] * N
# H = [0] + H
dp[0] = 0
for i in range(N):
    if i+1 < N:
        dp[i+1] = min(dp[i+1], dp[i] + abs(H[i] - H[i+1]))
    if i+2 < N:
        dp[i + 2] = min(dp[i + 2], dp[i] + abs(H[i] - H[i + 2]))

print(dp[N-1])