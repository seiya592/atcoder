def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)


N = II()
A = LIIS()

S = [0] * (N+1)
for i in range(1,N+1):
    S[i] = S[i-1] + A[i-1]

ans = 0
for i in range(N):
    ans += A[i] * (S[N] - S[i+1])
    ans %= 10**9 + 7

print(ans)