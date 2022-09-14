"""
2022/08/27 20:49:20
"""
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
TXA = LLIIS(N)

# TXA.sort(key=lambda x:(x[0],x[2]))
MAX= 10**5
# dp[時間][Xにいる時の] = 最大値
dp = [[-INF]*5 for _ in range(MAX+1)]
dp[0][0] = 0
now = 0 #現在のT　ここまで見た

for t in range(1,MAX+1):
    for x in range(5):
        dp[t][x] = max(dp[t-1][x], dp[t-1][max(x-1,0)], dp[t-1][min(4,x+1)])
        if now < N and TXA[now][0] == t and TXA[now][1] == x:
            dp[t][x] += TXA[now][2]
            now += 1
print(max(dp[MAX]))