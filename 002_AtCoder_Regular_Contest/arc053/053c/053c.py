def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)

N = II()
LAB = []    # 最終結果,増加,減少
MAB = []
for _ in range(N):
    a, b =IIS()
    if a-b < 0:
        LAB.append([a-b, a, b])
    else:
        MAB.append([a-b, a, b])

LAB.sort(key=lambda x:x[1])
MAB.sort(key=lambda x:x[2], reverse=True)

old = 0
m = 0

for l, a, b in LAB:
    m = max(m, old + a)
    old += l
for n, a, b in MAB:
    m = max(m, old + a)
    old += n

print(m)