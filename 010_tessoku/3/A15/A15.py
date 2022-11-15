"""
2022/10/13 19:44:38
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


def COMPRESS(arr): return {e: i for i, e in enumerate(sorted(set(arr)), start=1)}
# 一次元リスト座標復元用
def UNCOMPRESS(arr): return {i: e for i, e in enumerate(sorted(set(arr)))}

N = II()
A = LIIS()

C = COMPRESS(A)
ans = []
for a in A:
    ans.append(C[a])
print(*ans)