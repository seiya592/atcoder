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

def factorization2(n):
    arr = [0] * (n+1)
    for i in range(2,n+1):
        if arr[i]:
            continue
        j = 1
        while i*j <= n:
            arr[i*j] += 1
            j+=1
    return arr

N, K = IIS()
t = factorization2(N)
ans = 0
for a in t:
    if a >= K:
        ans+=1
print(ans)