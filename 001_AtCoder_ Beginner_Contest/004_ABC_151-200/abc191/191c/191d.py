
"""
ある点[x,y]を基準として[x,y][x+1,y][x,y+1][x+1,y+1]を見る

①中心は頂点ではない
##
##

②中心は頂点
##
.#

③中心は頂点ではない
##
..

④中心は頂点
..
#.

#の個数が1/3ならば頂点となる

"""



# 解説読み


def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [I() for _ in range(n)]
import sys
sys.setrecursionlimit(10000000)


H, W = IIS()
S = LLIIS(H)

ans = 0
for i in range(H-1):  #端は見ない
    for j in range(W-1):  #端は見ない
        cnt = 0
        for x, y in [[i,j],[i+1,j],[i,j+1],[i+1,j+1]]:
            if S[x][y] == '#':
                cnt += 1
        if cnt == 1 or cnt == 3:
            ans += 1
print(ans)