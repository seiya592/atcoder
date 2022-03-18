def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)


N, M = IIS()
A = [True] * (N + 1)
for _ in range(M):
    a = II()
    A[a] = False


dp = [0] * (N + 1)
dp[0] = 1

if A[1]:
    dp[1] = 1

for i in range(2,N+1):
    if A[i]:
        dp[i] = (dp[i-1] + dp[i-2]) % (10 ** 9 + 7)
    else:
        dp[i] = 0

print(dp[N])