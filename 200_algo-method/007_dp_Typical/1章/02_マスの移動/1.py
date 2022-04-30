def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)


N = II()
A = LIIS()

dp = [10 ** 10] * N
dp[0] = 0
dp[1] = A[1]
for n in range(2,N):
    dp[n] = min(dp[n-1] + A[n], dp[n-2] + A[n] * 2)
print(dp[N-1])