def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)

import math

N, X = IS()
N = int(N)
S = I()
x = X
zyousu = 0

while True:

    tmp = ''
    for s in x:
        ss = int(s) // 2
        tmp = tmp + str(ss)
    zyousu += 1
    x = tmp
    if len(tmp) < 2:
        if int(tmp) == 0:
            break

hasu = int(X) - (2 ** zyousu)

for i in range(N):
    s = S[i]
    if s == 'U':
        zyousu = max(zyousu-1 ,0)
        hasu = hasu >> 1
        continue

    zyousu += 1
    hasu = hasu * 2
    if s == 'R':
        hasu += 1

print(2 ** zyousu + hasu)