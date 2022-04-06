def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(10000000)


N = II()
XYH = LLIIS(N)
XYH.sort(key=lambda x:-x[2])


for cx in range(0,101):
    for cy in range(0, 101):
        x,y,h = XYH[0]
        H = h + abs(x-cx) + abs(y-cy)
        for x,y,h in XYH[1:]:
            if not max(H-abs(cx-x)-abs(cy-y),0) == h:
                break
        else:
            print(cx,cy,H)
            exit()
