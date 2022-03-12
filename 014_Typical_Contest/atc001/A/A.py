def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(1000000)

H, W = IIS()
C = [I() for _ in range(H)]
search = [[False] * W for _ in range(H)]


def dfs(i,j):
    search[i][j] = True
    for y, x in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
        if not(0<=y<H and 0<=x<W):
            continue

        if C[y][x] == '#':
            continue

        if not search[y][x]:
            dfs(y, x)
            continue


# スタート位置探す
for i, c in enumerate(C):
    if c.find('s') >= 0:
        s = [i, c.find('s')]
        break

for i, c in enumerate(C):
    if c.find('g') >= 0:
        g = [i, c.find('g')]
        break

search[s[0]][s[1]] = True
dfs(s[0], s[1])
if search[g[0]][g[1]]:
    print('Yes')
else:
    print('No')
