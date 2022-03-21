def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)


S = I()

ACGT = ['A','C','G','T']
cnt = 0
ans = 0
for s in S:
    if s in ACGT:
        cnt += 1
    else:
        ans = max(ans,cnt)
        cnt = 0
else:
    ans = max(ans,cnt)

print(ans)