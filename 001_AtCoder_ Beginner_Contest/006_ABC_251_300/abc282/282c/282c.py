"""
2022/12/17 22:05:04
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
#import pypyjit
#pypyjit.set_param('max_unroll_recursion=-1')        
sys.setrecursionlimit(500000)
INF = 10**17


N = II()
S = I()

flg = 0
ans = []
for s in S:
    if s == '"':
        flg ^= 1

    if not flg and s == ',':
        ans.append('.')
    else:
        ans.append(s)
print(''.join(ans))
