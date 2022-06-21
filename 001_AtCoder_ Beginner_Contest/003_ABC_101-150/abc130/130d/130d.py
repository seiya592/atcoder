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

N,K = IIS()
A = LIIS()

left = 0
right = 0

ans = 0
total = 0
while left < N:
    while right < N and total < K:
        total += A[right]
        right += 1

    if total >= K:
        ans += N-(right-1)
    else:
        break

    total -= A[left]
    left += 1
print(ans)

