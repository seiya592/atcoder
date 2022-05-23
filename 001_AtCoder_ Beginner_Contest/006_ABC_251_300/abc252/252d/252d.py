def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)
import collections

N = II()
A = LIIS()

#全体の組み合わせ数
ALL = N*(N-1)*(N-2) // 6

d = collections.defaultdict(int)
for a in A:
    d[a] += 1

d = dict(d)

m = 0

#1つのみ重複、全部重複すべてのパターンを数える
for k,v in d.items():
    #１つのみ重複
    if v >= 2:
        m += v*(v-1) // 2 * (N-v)

    #全部重複
    if v >= 3:
        m += v*(v-1)*(v-2) // 6
print(ALL-m)