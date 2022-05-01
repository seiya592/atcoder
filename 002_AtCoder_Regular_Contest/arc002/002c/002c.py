def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)


N = II()
C = I()

cmd = []
for i in ['A','B','X','Y']:
    for j in ['A', 'B', 'X', 'Y']:
        cmd.append([i,j])

ans = 10**10
for r in cmd:
    for l in cmd:
        dp = [10**10] * (N+1)
        dp[0] = 0
        for n in range(1,N+1):
            dp[n] = min(dp[n],dp[n-1]+1)
            if n >= 2 and (C[n-1] == r[1] and C[n-2] == r[0]) or (C[n-1] == l[1] and C[n-2] == l[0]):
                dp[n] = min(dp[n],dp[n-2]+1)
        ans = min(dp[N],ans)
print(ans)