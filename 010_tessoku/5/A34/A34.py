"""
2022/11/16 20:00:53
"""
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


N,X,Y = IIS()
A = LIIS()
A_MAX = max(A)
Grundy = [0] * (A_MAX+1)

for i in range(1,A_MAX+1):
    s = set()
    if i-X >= 0:
        s.add(Grundy[i-X])
    if i-Y >= 0:
        s.add(Grundy[i-Y])

    for j in range(0,3):
        if j not in s:
            Grundy[i] = j
            break

ans = 0
for a in A:
    ans ^= Grundy[a]
print('First' if ans else 'Second')