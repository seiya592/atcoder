def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
def LI(n): return [I() for _ in range(n)]
def PLUS(x,y): return [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]
import sys
sys.setrecursionlimit(500000)
INF = 10**10


N = II()
A = LIIS()
cnt = [0] * 5
for a in A:
    cnt[0] += 1
    tmp = [0] * 5
    for i in range(5):
        tmp[min(4,i+a)] += cnt[i]

    cnt = tmp
print(cnt[4])