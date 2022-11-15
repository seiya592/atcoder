"""
2022/11/09 18:12:26
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


H,W = IIS()
S = LI(H)

done = [[0] * W for _ in range(H)]

def dfs(h,w,black,white):
    if S[h][w] == '.':
        white += 1
    else:
        black += 1
    done[h][w] = 1

    for x,y in PLUS(h,w):
        if 0<=x<H and 0<=y<W and not done[x][y]:
            if S[h][w] == S[x][y]:
                continue
            black, white = dfs(x,y,black,white)

    return black, white

ans = 0
for h in range(H):
    for w in range(W):
        if done[h][w]:
            continue
        a,b = dfs(h,w,0,0)
        ans += a * b
print(ans)