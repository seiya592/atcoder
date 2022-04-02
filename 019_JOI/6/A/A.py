def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
# sys.setrecursionlimit(10000000)
# https://www.ioi-jp.org/joi/2006/2007-ho-prob_and_sol/2007-ho.pdf#page=2

N, K = IIS()
sum = [0] * (N+1)

for i in range(1,N+1):
    n = II()
    sum[i] = sum[i-1] + n

ans = 0
for i in range(0,N+1-K):
    ans = max(ans,sum[i+K] - sum[i])
print(ans)