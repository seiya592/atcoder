def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)
def has_bit(n, i):
    return (n & (1<<i)) > 0
from collections import defaultdict

N, X = IIS()
A = []
B = []

for i in range(N):
    n = II()
    if i % 2 == 0:
        A.append(n)
    else:
        B.append(n)

cost = defaultdict(int) # 初期値をすべて０にする
ans = 0
for i in range(1<<len(A)):
    tmp = 0
    for j in range(len(A)):
        if has_bit(i,j):
            tmp += A[j]
    cost[tmp] += 1

for i in range(1<<len(B)):
    tmp = 0
    for j in range(len(B)):
        if has_bit(i,j):
            tmp += B[j]

    ans += cost[X-tmp]

print(ans)