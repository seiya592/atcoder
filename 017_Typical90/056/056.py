def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
def LI(n): return [I() for _ in range(n)]
def PLUS(x,y): return [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]
import sys
sys.setrecursionlimit(500000)
INF = 10**10


N,S = IIS()
AB = LLIIS(N)

dp = [[0] * (S+2) for _ in range(N+1)]
dp[0][0] = 1
for n in range(N):
    for i in range(S):
        dp[n+1][min(i+AB[n][0],S+1)] += dp[n][i]
        dp[n + 1][min(i + AB[n][1], S + 1)] += dp[n][i]
pass

if not dp[N][S]:
    print('Impossible')
    exit()

ans = []
#復元
now = S
for n in range(N,0,-1):
    if now - AB[n-1][0] >= 0:
        if dp[n-1][now - AB[n-1][0]]:
            now -= AB[n-1][0]
            ans.append('A')
        else:
            now -= AB[n - 1][1]
            ans.append('B')
    else:
        now -= AB[n-1][1]
        ans.append('B')

print(''.join(reversed(ans)))