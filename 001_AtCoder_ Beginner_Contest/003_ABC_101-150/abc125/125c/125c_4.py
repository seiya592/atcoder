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
import math

#挟み込み累積和?

N = II()
A = LIIS()

left = [0] * (N+2)
right = [0] * (N+2)

for i in range(N):
    left[i+1] = math.gcd(left[i], A[i])

for i in reversed(range(N)):
    right[i+1] = math.gcd(right[i+2], A[i])

ans = 0
for i in range(N):
    ans = max(ans, math.gcd(left[i], right[i+2]))
print(ans)