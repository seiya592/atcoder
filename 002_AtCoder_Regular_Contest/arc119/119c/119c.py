"""
2022/10/24 18:44:34
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

S = [0]

t = 1
for a in A:
    if t%2:
        S.append(S[-1] + a)
    else:
        S.append(S[-1] - a)
    t += 1

D = collections.defaultdict(int)

for s in S:
    D[s] += 1

ans = 0
for k,v in D.items():
    ans += (v*(v-1)) // 2
print(ans)