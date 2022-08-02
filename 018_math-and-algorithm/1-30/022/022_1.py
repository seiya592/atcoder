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

cnt = [0] * (10**5)
for a in A:
    cnt[a] += 1

ans = 0
for i in range(1,50000):
    ans += cnt[i] * cnt[10**5-i]

#50000は組み合わせ nC2
ans += cnt[50000] * (cnt[50000]-1) // (2*1)
print(ans)