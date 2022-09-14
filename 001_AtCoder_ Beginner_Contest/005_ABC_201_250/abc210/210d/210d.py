"""
2022/09/05 17:18:32
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
INF = 10**17


H,W,C = IIS()
A = LLIIS(H)

def calc(A):
    dp = [[INF]*W for _ in range(H)]
    #dp[h][w] = 駅を立てる場合 or レールを別の所から敷く どちらかの最安値

    for i in range(H):
        for j in range(W):
            t1 = dp[i-1][j] if i else INF
            t2 = dp[i][j-1] if j else INF
            dp[i][j] = min(t1+C, t2+C, A[i][j]) #隣なので距離コストは常にC

    #レールor駅が置いてあるdp[i-1][j] or dp[i][j-1] の隣に駅を立てる場合の最安値
    ans = INF

    for i in range(H):
        for j in range(W):
            t1 = dp[i-1][j] if i else INF
            t2 = dp[i][j-1] if j else INF
            ans = min(ans, min(t1, t2)+C+A[i][j])
    return ans
AA = [a for a in reversed(A)]
print(min(calc(A), calc(AA)))