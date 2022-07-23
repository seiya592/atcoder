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


N, T = IIS()
AB = LLIIS(N)
AB.sort(key=lambda x:x[0])

dp = [[-INF] * (T+1) for _ in range(N+1)]
dp[0][0] = 0
for n in range(N):
    for t in range(T+1):
        if dp[n][t] == -INF:
            continue
        # 食べない
        dp[n+1][t] = max(dp[n][t], dp[n+1][t])

        if t == T:
            continue
        #食べる
        dp[n+1][min(t+AB[n][0],T)] = max(dp[n][t] + AB[n][1], dp[n+1][min(t+AB[n][0],T)])
print(max(dp[-1]))