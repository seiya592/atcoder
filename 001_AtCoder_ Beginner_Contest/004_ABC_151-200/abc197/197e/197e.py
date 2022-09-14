"""
2022/09/02 23:23:10 → 23:37:55
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
INF = 10**16


N = II()
XC = LLIIS(N)

XC.sort(key=lambda x:(x[1], x[0]))

D = dict()
now = INF
for x,c in XC:
    if now != c:
        D[c] = [x, x]
        now = c
    else:
        D[c][0] = min(D[c][0], x)
        D[c][1] = max(D[c][1], x)

K = sorted(D.keys())
dp = [[INF, INF] for _ in range(len(K)+ 1)]
dp[0][0] = 0
dp[0][1] = 0
old_l = 0
old_r = 0
for i, k in enumerate(D.keys(), start=1):
    l = D[k][0]
    r = D[k][1]

    dp[i][0] = min(dp[i-1][0] + abs(old_l - r), dp[i-1][1] + abs(old_r - r)) + abs(l-r)
    dp[i][1] = min(dp[i-1][0] + abs(old_l - l), dp[i-1][1] + abs(old_r - l)) + abs(l-r)

    old_l = l
    old_r = r

print(min(dp[-1][0] + abs(old_l), dp[-1][1] + abs(old_r)))