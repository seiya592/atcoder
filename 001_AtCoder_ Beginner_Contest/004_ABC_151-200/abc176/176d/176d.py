import collections


def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [I() for _ in range(n)]
import sys
sys.setrecursionlimit(100000)
PLUS = [[1,0],[0,1],[-1,0],[0,-1]]

#33m 非解説AC
#変数のx,y間違いで時間かかった

H,W = IIS()
Ch,Cw = IIS()
Dh,Dw = IIS()
Ch -= 1
Cw -= 1
Dh -= 1
Dw -= 1

S = LLIIS(H)

INF = 10**10

def check(x,y):
    if 0<=x<H and 0<=y<W:
        return True
    return False


dist = [[INF]*W for _ in range(H)]
dist[Ch][Cw] = 0
Q = collections.deque()
Q.append((Ch,Cw))
done = [[False]*W for _ in range(H)]
while len(Q) > 0:
    x,y = Q.popleft()
    if done[x][y]:
        continue
    done[x][y] = True

    for a, b in PLUS:
        i = x+a
        j = y+b

        if check(i,j) and not done[i][j]:
            if S[i][j] != '#':
                # if dist[i][j] > dist[x][y]: ←なくてもいい
                dist[i][j] = dist[x][y]
                Q.appendleft((i,j))

            else:
                for c in range(x-2, x+3):
                    for d in range(y-2, y+3):
                        if check(c,d) and not done[c][d] and S[c][d] == '.':
                            if dist[c][d] > dist[x][y] + 1:
                                dist[c][d] = dist[x][y] + 1
                                Q.append((c,d))


print(dist[Dh][Dw] if dist[Dh][Dw] != INF else -1)