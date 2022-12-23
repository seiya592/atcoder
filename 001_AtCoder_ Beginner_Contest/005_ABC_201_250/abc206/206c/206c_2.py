"""
2022/11/24 21:38:45
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


N = II()
A = LIIS()

#総数
ans = (N*(N-1)) // 2

#重複の組み合わせを消す
D = collections.defaultdict(int)

for a in A:
    D[a] += 1

D = dict(D)
for k,v in D.items():
    ans -= (v * (v-1)) // 2
print(ans)