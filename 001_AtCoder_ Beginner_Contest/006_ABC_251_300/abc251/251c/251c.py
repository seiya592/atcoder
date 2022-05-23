def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)


N = II()
d = [0] * N
s = set()

sl = 0
for i in range(N):
    S, T = IS()
    T = int(T)
    s.add(S)
    if sl != len(s):
        d[i] = [T]
    else:
        d[i] = []
    sl = len(s)

print(d.index(max(d)) + 1)
