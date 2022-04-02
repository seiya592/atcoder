def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)


N = II()
A = LIIS()

# sum = [[0] * 2 for _ in range(N+1)]
sum = [0] * (N+1)
ma = [0] * (N+1)
step = [0] * (N+1)

tmp_max = 0
for i in range(1,N+1):
    sum[i] = sum[i-1] + step[i-1] + A[i-1]
    ma[i] = max(ma[i-1], step[i-1])
    step[i] = step[i-1] + A[i-1]

ans = 0
for i in range(1, N+1):
    ans = max(ans, sum[i], sum[i-1] + ma[i])

print(ans)