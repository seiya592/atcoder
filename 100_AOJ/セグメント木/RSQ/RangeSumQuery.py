def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(10000000)
import math

# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_B&lang=jp


N, Q = IIS()
Query = LLIIS(Q)

SEG_LEN = 2 ** (int(math.log2(N))+1)
seg = [0] * (SEG_LEN * 2)

def add(i,v):
    i += SEG_LEN
    seg[i] += v
    while True:
        i //= 2
        if i == 0:
            break
        seg[i] = seg[i*2] + seg[i*2+1]

def get_sum(l,r):
    l += SEG_LEN
    r += SEG_LEN
    ret = 0
    while l < r:
        if l % 2 == 1:
            ret += seg[l]
            l += 1
        if r % 2 == 1:
            ret += seg[r-1]
            r -= 1
        l //= 2
        r //= 2
    return ret

for q in Query:
    c, x, y = q
    if c == 0:
        add(x, y)
    else:
        print(get_sum(x, y+1))
pass

