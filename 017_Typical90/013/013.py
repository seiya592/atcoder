def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)
import heapq

# 解説AC

N,M = IIS()
E = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = IIS()
    E[a].append((b, c)) # 頂点、距離
    E[b].append((a, c))

dist = [-1] * (N+1)
dist[1] = 0     #初期の町は０

done = [False] * (N + 1)
done[0] = True  # ０は使わない

Q = []
heapq.heappush(Q,(0, 1))     # 距離, 頂点


while len(Q) > 0:
    d, i = heapq.heappop(Q) # 最もコストが小さい町
    if done[i]:
        continue    # 訪問済みなら飛ばす
    done[i] = True

    for j, c in E[i]:
        if dist[j] == -1 or dist[j] > dist[i] + c:
            dist[j] = dist[i] + c
            heapq.heappush(Q,(dist[j], j))


# ゴールからの最短経路を求める
dist2 = [-1] * (N+1)
dist2[N] = 0     #初期の町は０

done2 = [False] * (N + 1)
done2[0] = True  # ０は使わない

Q = []
heapq.heappush(Q,(0, N))     # 距離, 頂点


while len(Q) > 0:
    d, i = heapq.heappop(Q) # 最もコストが小さい町
    if done2[i]:
        continue    # 訪問済みなら飛ばす
    done2[i] = True

    for j, c in E[i]:
        if dist2[j] == -1 or dist2[j] > dist2[i] + c:
            dist2[j] = dist2[i] + c
            heapq.heappush(Q,(dist2[j], j))

for i in range(1,N+1):
    print(dist[i] + dist2[i])