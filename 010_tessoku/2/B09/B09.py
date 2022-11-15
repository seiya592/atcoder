"""
2022/10/12 23:15:31
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
ALL = 1500

N = II()
S = [[0] * (ALL+2) for _ in range(ALL+2)]

for _ in range(N):
    a,b,c,d = IIS()
    S[a+1][b+1] += 1
    S[c+1][b+1] -= 1
    S[a+1][d+1] -= 1
    S[c+1][d+1] += 1

for i in range(1,ALL+1):
    for j in range(1,ALL+1):
        S[i][j] += S[i-1][j] + S[i][j-1] - S[i-1][j-1]

ans = 0
for s in S[:ALL+1]:
    ans += sum([(t != 0) for t in s[:ALL+1]])
print(ans)