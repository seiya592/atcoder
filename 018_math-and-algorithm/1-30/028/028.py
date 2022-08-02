def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
def LI(n): return [I() for _ in range(n)]
def PLUS(x,y): return [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]
def YES(): print('Yes'), exit()
def NO(): print('No'), exit()
import sys
sys.setrecursionlimit(500000)
INF = 10**10


N = II()
H = LIIS()

dp = [INF] * N
dp[0] = 0
dp[1] = abs(H[0]-H[1])
for n in range(2,N):
    dp[n] = min(dp[n-1] + abs(H[n-1] - H[n]), dp[n-2] + abs(H[n-2] - H[n]))
print(dp[N-1])