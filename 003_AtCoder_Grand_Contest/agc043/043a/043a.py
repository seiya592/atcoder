def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [I() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)
from collections import deque
import heapq
H, W = IIS()
S = LLIIS(H)
Q = deque()
dp = [[1000000] * (W) for _ in range(H)]
dp[0][0] = 1 if S[0][0] == '#' else 0

for x in range(H):
    for y in range(W):
        if x > 0:
            t = 1 if S[x][y] == '#' and S[x-1][y] == '.' else 0
            dp[x][y] = min(dp[x][y], dp[x-1][y] + t)
        if y > 0:
            t = 1 if S[x][y] == '#' and S[x][y-1] == '.' else 0
            dp[x][y] = min(dp[x][y], dp[x][y-1] + t)
print(dp[H-1][W-1])

# dp = [[1000000] * (W) for _ in range(H)]
# done = [[False] * (W) for _ in range(H)]
#
# # Q.append((0,0))
# heapq.heapify(Q)
# t = 1 if S[0][0] == '#' else 0
# dp[0][0] = t
# # heapq.heappush(Q,[t,1,0])
# # heapq.heappush(Q,[t,0,1])
# heapq.heappush(Q,[t,0,0])
#
# while len(Q) > 0:
#     c, x, y = heapq.heappop(Q)
#     if done[x][y]:
#         continue
#     done[x][y] = True
#     t = 1 if S[x][y] == '#' else 0
#     if x > 0 and y > 0:
#         dp[x][y] = min(dp[x-1][y], dp[x][y-1]) + t
#     elif x>0:
#         dp[x][y] = dp[x-1][y] + t
#     elif y>0:
#         dp[x][y] = dp[x][y-1] + t
#     else:
#         dp[x][y] = t
#
#     if y+1 < W:
#         t = 1 if S[x][y+1] == '#' else 0
#         heapq.heappush(Q, [dp[x][y]+t, x,y+1])
#         # Q.append([x,y+1])
#     if x+1 < H:
#         t = 1 if S[x+1][y] == '#' else 0
#         heapq.heappush(Q, [dp[x][y]+t, x+1, y])
#         # Q.appendleft([x+1,y])
#
# print(dp[H-1][W-1])