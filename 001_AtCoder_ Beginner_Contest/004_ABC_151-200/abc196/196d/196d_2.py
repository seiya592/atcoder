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
INF = 10**10


H,W,A,B = IIS()

done = [[False] * W for _ in range(H)]
def dfs(x,y,a,b):
    """
    :param x: 座標
    :param y:
    :param a: Aの畳を使っている枚数
    :param b: Bの畳を使っている枚数
    :return:
    """
    ans = 0
    if b > 0:
        done[x][y] = True
        flg = True
        for i in range(H):
            for j in range(W):
                if not done[i][j]:
                    ans += dfs(i,j,a,b-1)
                    flg = False
                    break
            else:
                continue
            break
        done[x][y] = False
        if flg:
            return 1

    if a > 0:
        # 縦に置く
        if x+1 < H and not done[x+1][y]:
            done[x][y] = True
            done[x+1][y] = True
            flg = True
            for i in range(H):
                for j in range(W):
                    if not done[i][j]:
                        ans += dfs(i, j, a-1, b)
                        flg = False
                        break
                else:
                    continue
                break
            done[x][y] = False
            done[x + 1][y] = False
            if flg:
                return 1

        if y+1 < W and not done[x][y+1]:
            done[x][y] = True
            done[x][y+1] = True
            flg = True
            for i in range(H):
                for j in range(W):
                    if not done[i][j]:
                        ans += dfs(i, j, a - 1, b)
                        flg = False
                        break
                else:
                    continue
                break
            done[x][y] = False
            done[x][y+1] = False
            if flg:
                return 1
    return ans

print(dfs(0,0,A,B))