def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(10000000)




N,M = IIS()
if not M:
    print(1)
    exit()
A = LIIS()

A.sort()
t = []

tmp = 1
for i in range(0,M):
    tt = A[i] - tmp
    if tt:
        t.append(tt)
    tmp = A[i] + 1
else:
    if N - A[-1]:
        t.append(N-A[-1])

# t_s = list(set(t))

# gcd = t_s[0]
# for s in t_s:
#     gcd = math.gcd(gcd,s)
if not t:
    print(0)
    exit()
m = min(t)

ans = 0
for tt in t:
    if tt % m == 0:
        ans += tt // m
    else:
        ans += tt//m + 1

print(ans)