"""
2022/10/13 19:13:01
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


N, K = IIS()
A = LIIS()

S = [0]
for a in A:
    S.append(S[-1] + a)

l = 0
r = 0
ans = 0
while l < N:
    while r +1 < N + 1 and S[r+1] - S[l] <= K:
        r += 1
    ans += r - l
    l += 1
    r = max(r, l)
print(ans)