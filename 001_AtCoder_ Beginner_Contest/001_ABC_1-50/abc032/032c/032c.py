def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
def LI(n): return [I() for _ in range(n)]
def PLUS(x,y): return [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]
import sys
sys.setrecursionlimit(100000)
INF = 10**10


N, K = IIS()
S = []
for _ in range(N):
    S.append(II())
if S.count(0) > 0:
    print(N)
    exit()
if K == 0:
    tmp = []
    for i,s in enumerate(S):
        if not s:
            tmp.append(i)

    print(tmp[-1] - tmp[0]+1 if tmp else 0)
    exit()


tmp = S[0]

left = 0
right = 0
ans = 0
while left < N:

    while right < N-1 and tmp*S[right+1] <= K:
        right += 1
        tmp *= S[right]

    if tmp <= K:
        ans = max(ans, right-left+1)
        tmp //= S[left]
        left += 1
    else:
        tmp //= S[left]
        left += 1
        right = left
        tmp = S[left-1]

print(ans)

