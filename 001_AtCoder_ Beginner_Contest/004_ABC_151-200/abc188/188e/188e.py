def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)


N,M = IIS()
A = LIIS()
E = [[] for _ in range(N+1)]
for _ in range(M):
    x,y = IIS()
    E[x].append(y)

dp = [10**10] * (N+1)
ans = -10**10

# X→Yの有向辺で絶対にX<YのDAGなのを利用する
for i, e in enumerate(E[1:],start=1):
    ans = max(A[i - 1] - dp[i], ans)
    dp[i] = min(dp[i], A[i - 1])
    for ee in e:
        dp[ee] = min(dp[ee],dp[i])
print(ans)