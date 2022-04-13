def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(10000000)


N = II()
A = LIIS()
A.sort()
#累積和
s = [0] * (N + 1)
for i , a in enumerate(A):
    s[i+1] = s[i] + a

ans = 0
for i in range(N):
    ans += s[N] - s[i] - (A[i] * (N - i))
print(ans)