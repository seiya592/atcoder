"""
2022/09/03 20:35:19
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


N,M = IIS()
A = LIIS()

S = [0] * (N+1)

for i,a in enumerate(A, start=1):
    S[i] += S[i-1] + a

l = 0
r = M

#初期設定
TMP = 0
Y = 0
for i in range(1,M+1):
    Y += A[i-1] * i
TMP = Y
ans = Y
for i in range(M+1,N+1):
    ans = max(ans, TMP)
    TMP += A[i-1] * M
    TMP -= S[i-1] - S[i-M-1]
print(max(ans,TMP))