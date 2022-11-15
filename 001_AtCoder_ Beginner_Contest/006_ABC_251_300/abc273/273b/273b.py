"""
2022/10/15 20:52:39
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



X,K = IS()

X = list(reversed(X)) + ['0']
K = int(K)

for k in range(K):
    if k < len(X):
        if int(X[k]) >= 5:
            X[k+1] = str(int(X[k+1]) + 1)
        X[k] = '0'

for i in range(len(X)-1):
    if X[i] == '10':
        X[i+1] = str(int(X[i+1]) + 1)
        X[i] = '0'

X = list(reversed(X))
X = ''.join(X)
ans = int(X)
print(ans)