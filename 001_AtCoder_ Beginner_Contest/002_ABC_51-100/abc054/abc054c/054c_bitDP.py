def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)
def has_bit(n, i):
    return (n & (1<<i)) > 0

N, M = IIS()
E = [[False] * N for _ in range(N)]

# 辺をリストに格納
for _ in range(M):
    a, b = IIS()
    E[a-1][b-1] = True
    E[b-1][a-1] = True

ALL = 2 ** N

ans = [[0] * N for _ in range(ALL)]

# スタートは1から
ans[1][0] = 1

for n in range(ALL):
    for i in range(N):  # スタート地点
        for j in range(N): # ゴール地点
            if E[i][j]: # 辺が存在する
                if has_bit(n,i): # スタート地点を踏んでいる
                    if not has_bit(n,j): # ゴール地点を踏んでいない
                        ans[n + (1 << j)][j] += ans[n][i]   # スタート地点でゴールしている会があれば＋１

print(sum(ans[ALL-1]))
