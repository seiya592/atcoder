"""
2022/11/05 20:57:29
"""
def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return tuple(map(int, input().split()))
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
P = LIIS()

import itertools

#後ろから見て低くなっているところを見る
c = INF
T = []
a = 0
for i in range(N-1,-1,-1):
    if c > P[i]:
        T.append(P[i])
        c = P[i]
    else:
        T.append(P[i])
        a = P[i]

        break

T.sort()
#最後の文字より１つ小さい数字を探す
s = 0
for t in T:
    if t < a:
        s = max(s,t)
T.pop(T.index(s))

if i:
    print(*P[:i], s, *sorted(T,reverse=True))
else:
    print(s, *sorted(T, reverse=True))
