def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)


N = 10
A = []
island = 0

for _ in range(N):
    s = I()
    island += s.count('o')
    A.append(s)


def dfs(i,j):
    global tmp
    tmp += 1
    done[i][j] = True
    for x, y in [[0,1],[1,0],[0,-1],[-1,0]]:
        if 0<=x+i<10 and 0<=y+j<10 and not done[x+i][y+j] and A[x+i][y+j] == 'o':
            dfs(x+i,y+j)




for i in range(N):
    for j in range(N):
        if A[i][j] == 'x':
            tmp = 0
            done = [[False] * N for _ in range(N)]
            dfs(i,j)

            if tmp == (island+1):
                print('YES')
                exit()
print('NO')