def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)


# https://www.ioi-jp.org/joi/2009/2010-ho-prob_and_sol/2010-ho.pdf#page=2

N, M = IIS()
A = [0] * (N+1)
for i in range(2, N+1):
    A[i] = A[i-1] + II()

now = 1
ans = 0
for i in range(M):
    next = II() + now
    ans += A[max(now,next)] - A[min(now,next)]
    ans %= 10 ** 5
    now = next
print(ans)