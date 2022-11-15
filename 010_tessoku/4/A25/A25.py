"""
2022/10/24 19:33:25
"""
import collections


def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
def LI(n): return [I() for _ in range(n)]
def PLUS(x,y): return [[x+1,y],[x,y+1]]
def YES(): print('Yes'), exit()
def NO(): print('No'), exit()
def CEIL(x,y): return -(-x // y)    # 除算を小数点切り上げ
import sys
sys.setrecursionlimit(500000)
INF = 10**17


H, W = IIS()
C = LI(H)

dp = [[0] * W for _ in range(H)]
dp[0][0] = 1

for h in range(H):
    for w in range(W):
        if C[h][w] == '#':
            continue

        if h and w:
            dp[h][w] += dp[h-1][w]
            dp[h][w] += dp[h][w - 1]
        elif w:
            dp[h][w] += dp[h][w-1]
        elif h:
            dp[h][w] += dp[h - 1][w]
print(dp[-1][-1])


# Q = collections.deque()
# Q.append((0,0))

# while Q:
#     x,y = Q.popleft()
#
#     dp[x][y] += []
#
#     for x2,y2 in PLUS(x,y):
#         if x2<H and y2 < W and C[x2][y2] == '.':
#             Q.append((x2,y2))