import heapq


def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
def LI(n): return [I() for _ in range(n)]
def PLUS(x,y): return [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]
import sys
sys.setrecursionlimit(500000)
INF = 10**10


N = II()
A = LIIS()

#最大値側のありうる範囲
max_sum = [0] * (N+1)
max_sum[0] = sum(A[0:N])

maxQ = []
heapq.heapify(maxQ)
for a in A[0:N]:
    heapq.heappush(maxQ,a)

for i,a in enumerate(A[N:N*2],start=1):
    heapq.heappush(maxQ,a)
    max_sum[i] = max_sum[i-1] + a - heapq.heappop(maxQ)

#最小値側のありうる範囲
min_sum = [0] * (N+1)
min_sum[-1] = sum(A[N*2:N*3])
minQ = []
heapq.heapify(minQ)
for a in A[N*2:N*3]:
    #大きい値をとりたいのでマイナスを入れる
    heapq.heappush(minQ, -a)

for i,a in enumerate(reversed(A[N:N*2]),start=1):
    heapq.heappush(minQ, -a)
    min_sum[-1-i] = min_sum[-i] + a + heapq.heappop(minQ)

ans = -(INF * 10 ** 10)
for i,j in zip(max_sum,min_sum):
    ans = max(ans, i - j)
print(ans)