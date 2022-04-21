def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)


N = II()

dp = [0] * max((N+1),3)
dp[2] = 1

#もらうDP

for n in range(3,N+1):
    dp[n] = (dp[n-1] + dp[n-2] + dp[n-3]) % 10007
print(dp[N-1])