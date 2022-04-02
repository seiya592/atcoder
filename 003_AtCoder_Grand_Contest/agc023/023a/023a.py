def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)
from collections import Counter
# 解説AC

N = II()
A = LIIS()
S = [0] * (N+1)

for i in range(1,N+1):
   S[i] += S[i-1] + A[i-1]

S_D = Counter(S)

ans = 0
for v in S_D.values():
    ans += (v * (v-1)) // 2

print(ans)