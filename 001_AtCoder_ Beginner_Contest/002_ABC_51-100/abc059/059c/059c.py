"""
2022/08/09 17:50:56
"""
def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
def LI(n): return [I() for _ in range(n)]
def PLUS(x,y): return [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]
def YES(): print('Yes'), exit()
def NO(): print('No'), exit()
import sys
sys.setrecursionlimit(500000)
INF = 10**10


N = II()
A = LIIS()

def calc(S):
    now = 0
    ans = 0
    for i in range(N):
        now += A[i]
        if S[i%2]:
            #プラスにする
            if now <= 0:
                ans += abs(now) + 1
                now = 1
        else:
            #マイナスにする
            if now >= 0:
                ans += abs(now) + 1
                now = -1
    return ans


print(min(calc([True,False]), calc([False,True])))