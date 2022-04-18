def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)


N,K = IIS()
R,S,P = IIS()
T = I()
d = {'r':P,'s':R,'p':S}
d_i = {'r':0,'s':1,'p':2}
#グループ分けを行う 同じグループ内では前の手は出せない
grp = [''] * K
for i, t in enumerate(T):
    grp[i%K] += t

ans = 0
for g in grp:
    dp = [[0] * 3 for _ in range(len(g))]
    dp[0][d_i[g[0]]] = d[g[0]]  #一番最初の手は点が入る
    #貰うDP
    for i, s in enumerate(g[1:], start=1):
        for h in range(3):
            dp[i][h] = max(dp[i-1][(h+1)%3],dp[i-1][(h+2)%3])   # 前回と違う手の大きいほうの値を採用
        dp[i][d_i[s]] += d[s]   #今回勝った手のスコアを足す
    ans += max(dp[len(g)-1])
print(ans)