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
AB = LLIIS(N)

cnt = [0] * (1000002)

for a,b in AB:
    cnt[a] += 1
    cnt[b+1] -= 1

#最大値求める
ans = 0
tmp = 0
for c in cnt:
    tmp += c
    ans = max(ans,tmp)

print(ans)