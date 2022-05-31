def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
def LI(n): return [I() for _ in range(n)]
def PLUS(x,y): return [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]
import sys
sys.setrecursionlimit(100000)
INF = 10**20



N, D = IIS()

# Dを素因数分解する ただしカウントするのは2,3,5だけで良い　それ以外がある場合は0％の為
count = []
for i in [2,3,5]:
    tmp = 0
    while D % i == 0:
        tmp += 1
        D //= i
    count.append(tmp)
else:
    if D != 1:
        #2,3,5以外で素因数分解ができる場合
        print(0)
        exit()

dp = [[[[0] * (count[2]+1) for _ in range(count[1]+1)] for _ in range(count[0]+1)] for _ in range(N+1)]
# dp[n回さいころをふった時に][2がx個][3がy個][5がz個] = になる確率
dp[0][0][0][0] = 1

#目による増加テーブル
plus = [[0,1,0,2,0,1],[0,0,1,0,0,1],[0,0,0,0,1,0]]

#配る
for n in range(N):

    for x in range(count[0]+1):
        for y in range(count[1]+1):
            for z in range(count[2]+1):
                for i in range(6):    #さいころの目
                    xx = min(count[0],x+plus[0][i])
                    yy = min(count[1], y + plus[1][i])
                    zz = min(count[2], z + plus[2][i])
                    dp[n+1][xx][yy][zz] += dp[n][x][y][z] / 6
print(dp[N][count[0]][count[1]][count[2]])