def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(10000000)


N = II()

dp = [10**6] * (N+1)
dp[0] = 0
for i in range(N+1):
    #配るDP
    if i + 1 <= N:
        dp[i+1] = min(dp[i] + 1,dp[i+1])

    j = 6
    t = 0
    while i+(j ** t) <= N:

        dp[i+j**t] = min(dp[i+j**t], dp[i] + 1)
        t += 1

    j = 9
    t = 0
    while i + (j ** t) <= N:
        dp[i +j**t] = min(dp[i + j**t], dp[i] + 1)
        t += 1

print(dp[N])