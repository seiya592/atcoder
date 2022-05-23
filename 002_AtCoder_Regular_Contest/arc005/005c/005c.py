import heapq


def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [I() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)
PLUS = [[1,0],[0,1],[-1,0],[0,-1]]

# 解説見ずに10分くらいで書けた　←えらい！！！！
# 1発でサンプル通った
# 本当はヒープキューじゃなくてデキューの両端に追加していくみたい
# 壁壊す系はこれかな？

H,W = IIS()
C = LLIIS(H)

B = [[-1]*W for _ in range(H)]

Q = []
heapq.heapify(Q)
for i in range(H):
    for j in range(W):
        if C[i][j] == 's':
            heapq.heappush(Q,(0,i,j))
            B[i][j] = 0
        if C[i][j] == 'g':
            goal = (i,j)

while len(Q) > 0:
    c,i,j = heapq.heappop(Q)

    for x,y in PLUS:
        if 0<=i+x<H and 0<=j+y<W and B[i+x][j+y] == -1:
            if C[i+x][j+y] == '#':
                B[i+x][j+y] = B[i][j] + 1
                heapq.heappush(Q,(c+1,x+i,y+j))
            else:
                B[i + x][j + y] = B[i][j]
                heapq.heappush(Q, (c, x + i, y + j))

print('YES' if B[goal[0]][goal[1]] <= 2 else 'NO')