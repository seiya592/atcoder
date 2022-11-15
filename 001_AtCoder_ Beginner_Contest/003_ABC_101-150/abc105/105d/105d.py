"""
2022/11/10 18:30:44
"""
import collections


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


N,M = IIS()
A = LIIS()

# 累積和をMで割った余りが同じ組み合わせを答えにする
ans = 0

s = 0
D = collections.defaultdict(int)
D[0] = 1
for a in A:
    s += a
    s %= M
    D[s] += 1

D = dict(D)

for _,v in D.items():
    if v >= 2:
        ans += (v * (v-1)) // 2
print(ans)