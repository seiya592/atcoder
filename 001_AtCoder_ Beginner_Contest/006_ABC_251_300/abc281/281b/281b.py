"""
2022/12/10 20:45:34
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


S = I()
if len(S) != 8:
    NO()

if not S[0].isupper():
    NO()

if not S[-1].isupper():
    NO()

if S[1:-1].isdigit() and 100000<=int(S[1:-1])<= 999999:
    YES()
NO()
