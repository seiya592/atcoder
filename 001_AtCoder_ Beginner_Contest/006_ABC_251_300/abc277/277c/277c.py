"""
2022/11/12 20:42:16
"""
import collections


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
def CEIL(x,y): return -(-x // y)    # 除算を小数点切り上げ
import sys
sys.setrecursionlimit(500000)
INF = 10**17


N = II()
E = collections.defaultdict(list)
done = collections.defaultdict(int)
for _ in range(N):
    a,b = IIS()
    E[a].append(b)
    E[b].append(a)
    done[a] = False
    done[b] = False

Q = collections.deque()
Q.append(1)

ans = 0
while Q:
    n = Q.popleft()
    if done[n]:
        continue
    done[n] = True
    ans = max(ans,n)
    for e in E[n]:
        if done[e]:
            continue
        Q.append(e)
print(ans)