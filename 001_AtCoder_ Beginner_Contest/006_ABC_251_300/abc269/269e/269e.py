"""
2022/09/17 20:39:37
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


N = II()

ans_i = -1
#縦を求める
ok = 1  #この含め右側にルークがおいていないところがある
ng = N+1 #この位置含め右側はルークで埋まっている
while abs(ok-ng) > 1:
    mid = (ok+ng) // 2
    print(f'? {ok} {mid-1} {1} {N}')
    ans = II()

    if ans == mid-ok:
        ok = mid
    else:
        ng = mid


ans_i = ok

# 横を求める
ok = 1
ng = N+1
while abs(ok-ng) > 1:
    mid = (ok+ng) // 2
    print(f'? {1} {N} {ok} {mid-1}')
    ans = II()

    if ans == mid-ok:
        ok = mid
    else:
        ng = mid



print(f'! {ans_i} {ok}')
