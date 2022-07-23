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
import sys
sys.setrecursionlimit(500000)
INF = 10**10


N,X,Y,Z = IIS()
A = LIIS()
B = LIIS()
AB = []
for i,(a,b) in enumerate(zip(A,B)):
    AB.append([i,a,b])

tmp = set()
ans = []

AB.sort(key=lambda x:(-x[1],x[0]))

x = 0
for i,a,b in AB:
    if x < X:
        tmp.add(i+1)
        ans.append(i+1)
        x += 1

y = 0
AB.sort(key=lambda x:(-x[2],x[0]))
for i,a,b in AB:
    if y < Y and not i+1 in tmp:
        tmp.add(i+1)
        ans.append(i+1)
        y += 1

AB.sort(key=lambda x:(-(x[1]+x[2]), x[0]))
z = 0
for i,a,b in AB:
    if z < Z and not i+1 in tmp:
        ans.append(i+1)
        z += 1

ans.sort()
for a in ans:
    print(a)