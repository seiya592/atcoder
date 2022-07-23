def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
def LI(n): return [I() for _ in range(n)]
def PLUS(x,y): return [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]
import sys
sys.setrecursionlimit(500000)
INF = 10**10

# 解説AC

N = II()
A = LIIS()

ALL = 60
ans = 0
for n in range(ALL+1):
    mask = 1 << n

    # n bit目の要素が０の数と１の数を求める
    # 0同士、1同士は影響が一切ない。あるのは1と0だけなので掛けた数が総数
    one = 0
    zero = 0
    for a in A:
        if a & mask:
            one += 1
        else:
            zero += 1

    ans += mask * one * zero
    ans %= 10**9+7
print(ans)