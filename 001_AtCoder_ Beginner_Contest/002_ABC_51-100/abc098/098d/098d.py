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
A = LIIS()

l = 0
r = 0

add_sum = 0
xor_sum = 0
ans = 0
while l < N:

    while r < N and add_sum + A[r] == xor_sum ^ A[r]:
        add_sum += A[r]
        xor_sum ^= A[r]
        r += 1

    ans += r-l

    add_sum -= A[l]
    xor_sum ^= A[l]

    l += 1
print(ans)