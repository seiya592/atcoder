def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)


N,M = IIS()
D = LIIS()

dp = [0] * (N+1)
dp[0] = 1
for n in range(N+1):
    for d in D:
        if d+n <= N:
            dp[n+d] += dp[n]
print('Yes' if dp[N] else 'No')