def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)


N = II()
S = I()

cnt = 0
add = 0
for s in S:

    if '(' == s:
        cnt += 1
    else:
        cnt -= 1

    add = min(add, cnt)

if add < 0:
    for _ in range(abs(add)):
        S = '(' + S

cnt = 0
for s in S:
    if '(' == s:
        cnt += 1
    else:
        cnt -= 1

if cnt > 0:
    for _ in range(cnt):
        S += ')'

print(S)