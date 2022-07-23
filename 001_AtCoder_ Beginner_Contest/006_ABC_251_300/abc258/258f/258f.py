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
#
#
# T = II()
#
# for _ in range(T):
#     B,K,Sx,Sy,Gx,Gy = IIS()
#
#     ans = 10**21
#
#     #直接行く
#     ans = min(ans, (abs(Sx-Gx) + abs(Sy - Gy))*K)
#
#     #Bのx軸ory軸を経由して行く
#     # if abs(Sx - B) < abs(Sy-B):
#     T1 = abs(Sx - B)
#     TX1 = B
#     TY1 = Sy
#     # else:
#     T2 = abs(Sy-B)
#     TX2 = Sx
#     TY2 = B
#
#     #ゴールから
#     # if abs(Sx - B) < abs(Sy-B):
#     T3 = abs(Gx - B)
#     TX3 = B
#     TY3 = Gy
#     # else:
#     T4 = abs(Gy - B)
#     TX4 = Gx
#     TY4 = B
#
#     tmp = 10 ** 21
#     for t, tx, ty in [[T1,TX1,TY1], [T2,TX2,TY2]]:
#         for g, gx, gy in [[T3, TX3, TY3], [T4, TX4, TY4]]:
#             tmp = min(tmp, (t+g)*K + abs(tx-gx) + abs(ty-gy))
#
#     ans = min(ans,tmp)
#     print(ans)