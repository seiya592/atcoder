"""
2022/08/07 19:05:49
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
INF = 10**10


N, K = IIS()
A = LIIS()

ALL = 40    # 2 ** 40 が大体10**13
ans = 0
for k in reversed(range(ALL+1)):
    one = 0
    zero = 0
    for a in A:
        if a & (1 << k):
            one += 1
        else:
            zero += 1

    if (1<<k) > K:
        ans += one * (1<<k)
    else:
        if one >= zero:
            ans += one * (1<<k)
        else:
            ans += zero * (1<<k)
            K -= (1<<k)
print(ans)