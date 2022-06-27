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

# 解説AC
# 5000*5000が間に合うのがわからなかった
# 範囲設定する際に最大値よりKのほうが大きい場合の例外を書かないといけない。（for文が一度も回らないため）


N,K = IIS()
AB = LLIIS(N)

ALL = max([max([a,b]) for a,b in AB])

if ALL <= K:
    print(N)
    exit()

# ALL = 5000

S = [[0] * (ALL+1) for _ in range(ALL+1)]
pass
#プロット
for a,b in AB:
    S[a][b] += 1

# 累積和横
for i in range(ALL+1):
    for j in range(ALL):
        S[i][j+1] += S[i][j]

#累積和縦
for j in range(ALL+1):
    for i in range(ALL):
        S[i+1][j] += S[i][j]

ans = 0
for i in range(1,ALL - K + 1):
    for j in range(1,ALL - K + 1):
        ans = max(ans, S[i+K][j+K] - S[i-1][j+K] - S[i+K][j-1] + S[i-1][j-1])
print(ans)
