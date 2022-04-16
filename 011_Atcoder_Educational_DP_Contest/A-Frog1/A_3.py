def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)


#もらうDP

N = II()
H = LIIS()
dp = [10**10] * N
dp[0] = 0
dp[1] = abs(H[0]-H[1])


for i in range(2,N):
    dp[i] = min(dp[i-1] + abs(H[i]-H[i-1]), dp[i-2] + abs(H[i]-H[i-2]))

print(dp[N-1])