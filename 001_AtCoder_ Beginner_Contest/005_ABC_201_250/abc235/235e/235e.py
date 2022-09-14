"""
2022/08/29 17:00:48
"""
import collections
import heapq


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
import sys
sys.setrecursionlimit(500000)
INF = 10**10


N,M,Q = IIS()
E = [[] for _ in range(N+1)]

for _ in range(M):
    a,b,c = IIS()
    E[a].append([b,c,Q])
    E[b].append([a,c,Q])

for q in range(Q):
    u,v,w = IIS()
    E[u].append([v,w,q])
    E[v].append([u,w,q])

done = [False] * (N+1)  #すでにつないだ点
cnt = 0 # Nになったら終了

#点１を初期状態とする
done[1] = True
cnt += 1

que = []
heapq.heapify(que)
#点1の隣接している辺を入れる
for e,w,q in E[1]:
    heapq.heappush(que,(w,e,q))

s = 0 # 最小全域木の重さの合計（ただし今回の問題には関係ない）

ans = [False] * (Q)
while cnt < N:
    w, n, q = heapq.heappop(que)

    # すでに繋がっていたら無視
    if done[n]:
        continue

    if q < Q:
        ans[q] = True   # もしq番目のqueryの辺が存在するなら採用されていた。
        continue

    # 繋がっておらず、queryの辺ではないなら 繋げる
    done[n] = True  # 繋げた
    cnt += 1        # 繋がった頂点の数+1
    s += w          # 木全体の合計（使わない)

    for e, c, p in E[n]:
        if done[e]: # すでに繋がっている場合は無視
            continue
        heapq.heappush(que,(c,e,p))


# # queryに答える
for a in ans:
    print('Yes' if a else 'No')
