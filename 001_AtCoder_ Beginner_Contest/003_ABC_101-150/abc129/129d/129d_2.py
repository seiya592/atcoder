def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
import bisect
sys.setrecursionlimit(10000000)


#二分探索を使う
H, W = LIIS()
S = [tuple(I()) for _ in range(H)]

row = [[-1] for _ in range(W)]    #row[i] = i列目のn番目に#が存在する
col = [[-1] for _ in range(H)]


for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            row[j].append(i)
            col[i].append(j)

for i in range(H):
    col[i] = col[i] + [W]
for j in range(W):
    row[j] = row[j] + [H]



ans = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == '.':
            x = bisect.bisect_left(row[j], i)
            y = bisect.bisect_left(col[i], j)

            tmp = -1
            tmp += row[j][x] - row[j][x-1] -1
            tmp += col[i][y] - col[i][y-1] -1

            if tmp == 14:
                a = 1
                pass

            ans = max(ans, tmp)

print(ans)