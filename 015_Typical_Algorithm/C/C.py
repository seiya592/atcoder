def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)
# https://atcoder.jp/contests/typical-algorithm/tasks/typical_algorithm_c

def has_bit(n, i):
    return (n & (1<<i)) > 0

N = II()
A = [LIIS() for _ in range(N)]
ALL = 2 ** N
INF = 10*100

cost = [[INF]* N for _ in range(ALL)]
cost[0][0] = 0

for i in range(ALL):
    for j in range(N):  # 現在位置
        for k in range(N): # これからの位置
            if not has_bit(i,k):    # これから行くところが訪問済みではない場合のみ処理
                if j != k:  # 同じところは無視
                    cost[i|1 << k][k] = min(cost[i|1 << k][k], cost[i][j] + A[j][k])

print(cost[ALL-1][0])