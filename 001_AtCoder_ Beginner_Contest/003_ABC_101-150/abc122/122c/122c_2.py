def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)


N, Q = IIS()
S = I()
s_len = len(S)
Query = [LIIS() for _ in range(Q)]

sum = [0] * (s_len + 1)
for i in range(2, s_len+1):
    sum[i] += sum[i-1]
    if S[i-1] == 'C' and S[i-2] == 'A':
        sum[i] += 1

for l, r in Query:
    print(sum[r] - sum[l])