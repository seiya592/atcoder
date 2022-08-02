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


N = II()
C = LIIS()

# 桁
D = N // min(C)
M = min(C)      # Cの最小
nowD = D
ans = []
for d in range(D):
    for i in reversed(range(1,10)):
        if N - ((nowD-1) * M) - C[i-1] >= 0:
            ans.append(str(i))
            nowD -= 1
            N -= C[i-1]
            break
print(''.join(ans))