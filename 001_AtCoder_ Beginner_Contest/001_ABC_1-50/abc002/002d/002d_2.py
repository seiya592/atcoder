def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)


#dfsで解いてみる

N,M = IIS()
E = [[i] for i in range(N+1)]
for _ in range(M):
    x,y = IIS()
    E[x].append(y)
    E[y].append(x)

lst = []
ans = 0
def dfs(n):
    global lst
    global ans
    if n == N+1:
        #最後まで行ったら
        flg = True
        for t in lst:
            for i in lst:
                if not i in E[t]:
                    flg = False
                    break

        if flg:
            ans = max(ans,len(lst))
    else:
        # まずはnを採用
        lst.append(n)
        dfs(n+1)

        #不採用
        lst = lst[:-1]
        dfs(n+1)
dfs(1)
print(ans)