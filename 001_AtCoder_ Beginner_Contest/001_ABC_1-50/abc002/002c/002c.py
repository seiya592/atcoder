def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(10000000)


import math
xa, ya, xb, yb, xc, yc = IIS()
#辺の長さ
ab = math.sqrt(abs(xa-xb) ** 2 + abs(ya-yb) ** 2)
ac = math.sqrt(abs(xa-xc) ** 2 + abs(ya-yc) ** 2)
bc = math.sqrt(abs(xc-xb) ** 2 + abs(yc-yb) ** 2)

#ヘロンの公式
s = (ab+bc+ac)/2
print(round(math.sqrt(s*(s-ab)*(s-ac)*(s-bc)),3))