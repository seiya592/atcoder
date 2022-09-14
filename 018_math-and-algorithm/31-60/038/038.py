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


N, Q = IIS()
A = LIIS()

B = [0]
for a in A:
    B.append(a+B[-1])

# こっちでも速度は変わらない
# B = [0] * (N+1)
# for i in range(N):
#     B[i+1] = B[i] + A[i]

for _ in range(Q):
    l,r = IIS()
    print(B[r]-B[l-1])
