def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)


N,K = IIS()
H = LIIS()

#配るDP
dp = [10**10] * N
dp[0] = 0
for i in range(N):
    for k in range(i+1,i+K+1):
        if k < N:
            dp[k] = min(dp[k],dp[i] + abs(H[i]-H[k]))
print(dp[N-1])