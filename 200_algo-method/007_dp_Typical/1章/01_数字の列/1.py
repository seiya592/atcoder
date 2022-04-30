def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)


N,X,Y = IIS()
dp = [0] * N
dp[0] = X
dp[1] = Y
for n in range(2,N):
    dp[n] = (dp[n-1] + dp[n-2]) % 100
print(dp[N-1])