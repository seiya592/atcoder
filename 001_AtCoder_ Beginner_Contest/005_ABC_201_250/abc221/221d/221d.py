def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)
def COMPRESS(arr): return {e: i for i, e in enumerate(sorted(set(arr)))}

N = II()
LOGIN = [LIIS() for _ in range(N)]
comptmp = []
for a, b in LOGIN:
    comptmp.extend([a, a+b])

comp = COMPRESS(comptmp)
compv = list(comp.keys())

# いもす法？
tmp = [0] * (len(comp))   # i日に変動した人数
ans = [0] * (N + 1)   # i人がログインしていた日数
for a, b in LOGIN:
    tmp[comp[a]] += 1
    tmp[comp[a+b]] -= 1

person = 0
for i in range(len(comp)-1):
    person += tmp[i]
    ans[person] += compv[i+1] - compv[i]

print(*ans[1:])