"""
2022/09/28 22:25:48
https://atcoder.jp/contests/code-festival-2015-morning-middle/tasks/cf_2015_morning_hard_a
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


N = II()
A = LIIS()

ans = 0

l = 0
r = N-1

l_s = A[l]
r_s = A[r]
while l != r:
    if l_s > r_s:
        ans += (r_s*2) + A[r-1] + 1
        r_s += A[r-1] + A[r-2] + 2
        r -= 2
    else:
        ans += (l_s * 2) + A[l + 1] + 1
        l_s += A[l + 1] + A[l + 2] + 2
        l += 2
print(ans)