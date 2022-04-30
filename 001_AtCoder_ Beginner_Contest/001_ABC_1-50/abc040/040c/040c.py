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

dp = [0] * N
dp[1] = abs(A[0] - A[1])

for n in range(2, N):
    dp[n] = min(dp[n-1] + abs(A[n]-A[n-1]), dp[n-2] + abs(A[n]-A[n-2]))
print(dp[N-1])