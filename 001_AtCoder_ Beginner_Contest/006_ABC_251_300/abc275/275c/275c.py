"""
2022/10/29 20:52:00
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
def CEIL(x,y): return -(-x // y)    # 除算を小数点切り上げ
import sys
sys.setrecursionlimit(500000)
INF = 10**17

S = LI(9)
ans = 0
for i in range(9):
    for j in range(9):  #左上の起点
        if S[i][j] == '.':
            continue

        # 右上候補を求める
        for x in range(9):
            for y in range(j+1,9):
                if S[x][y] == '.':
                    continue
                if i == x and j == y:
                    continue

                #左下の座標
                a = abs(i-x) + j    #横
                b = abs(j-y) + i    #縦
                if 0 <= b < 9 and 0 <= a < 9:
                    if S[b][a] == '.':
                        continue
                else:
                    continue

                n = y + abs(i-x)        # 横
                m = x + abs(j-y)           #縦
                if 0<=n < 9 and 0<=m < 9:
                    if S[m][n] == '.':
                        continue
                else:
                    continue

                T = set()
                T.add((i,j))
                T.add((x,y))
                T.add((b,a))
                T.add((m,n))
                if len(T) == 4:
                    ans += 1

print(ans)