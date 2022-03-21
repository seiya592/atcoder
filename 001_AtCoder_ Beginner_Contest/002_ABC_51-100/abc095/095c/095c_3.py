def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)


A,B,C,X,Y = IIS()
ans = 10**100
for i in range(0, max(X,Y)*2 + 1, 2):   #1枚ずつ買う理由がないため２Step
    cost = i * C    #ピザcをi毎買う

    # Cで作成して残りの必要数
    a = X - (i//2)
    b = Y - (i//2)

    if a > 0:
        cost += a * A
    if b > 0:
        cost += b * B

    ans = min(ans,cost)

print(ans)