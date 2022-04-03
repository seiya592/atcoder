def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)


x1, y1 = IIS()
x2, y2 = IIS()
x3, y3 = IIS()
ansx = 0
ansy = 0

if x1 == x2:
    ansx = x3
elif x1 == x3:
    ansx = x2
else:
    ansx = x1

if y1 == y2:
    ansy = y3
elif y1 == y3:
    ansy = y2
else:
    ansy = y1

print(ansx, ansy)