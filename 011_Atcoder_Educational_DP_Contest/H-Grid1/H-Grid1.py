def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
import collections
sys.setrecursionlimit(10000000)


H, W = IIS()
G = [I() for _ in range(H)]

pattern = [[0] * (W+1) for _ in range(H+1)]
Q = collections.deque()
Q.append([2, 1])
Q.append([1, 2])
pattern[1][1] = 1

while len(Q) > 0:
    i, j = Q.popleft()

    if not(1<=i<=H and 1<=j<=W):
        continue
    if G[i-1][j-1] == '#':
        continue
    if pattern[i][j] == 0:
        pattern[i][j] = pattern[i-1][j] + pattern[i][j-1]
        Q.append([i,j+1])
        Q.append([i+1,j])

print(pattern[H][W] % ((10**9)+7))
