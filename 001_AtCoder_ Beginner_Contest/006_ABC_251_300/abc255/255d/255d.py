import bisect


def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
def LI(n): return [I() for _ in range(n)]
def PLUS(x,y): return [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]
import sys
sys.setrecursionlimit(100000)
INF = 10**10


N,Q = IIS()
A = LIIS()
A.sort()

#累積和
As = [0] * (N+1)
for i,a in enumerate(A,start=1):
    As[i] = As[i-1] + a

for _ in range(Q):
    x = II()
    ans = 0

    left = bisect.bisect_left(A,x)
    ans += (x * left) - As[left]

    right = bisect.bisect_right(A,x)
    ans += (As[-1] - As[right])- (x*(N-right))
    print(ans)
