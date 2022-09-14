"""
2022/09/06 17:06:42
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
import sys
sys.setrecursionlimit(500000)
INF = 10**17


N,T = IIS()
A = LIIS()

min_v = INF
now_v = INF
ans = 0

for a in A:
    if min_v > a:
        min_v = a
    else:
        if now_v == min_v-a:
            ans += 1
        elif now_v > min_v - a:
            ans = 1
            now_v = min_v - a
print(ans)