import heapq


def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
def LI(n): return [I() for _ in range(n)]
def PLUS(x,y): return [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]
import sys
sys.setrecursionlimit(500000)
INF = 10**10


N = II()
X = LIIS()
C = LIIS()

lst = [[i,0] for i in range(N+1)]

for x,c in zip(X,C):
    lst[x][1] += c

Q = [(c,n) for n,c in lst]
heapq.heapify(Q)

# lst.sort(key=lambda x:x[1])

P = [0] * (N+1)
# tmpC = [0] * (N+1)
idx = 0
done = [False] * (N+1)
done[0] = True
D = dict()
while Q:
   c,n = heapq.heappop(Q)
   if done[n]:
       continue

   # if tmpC[n]:
   #     c -= tmpC[n]
   #     tmpC[n] = 0
   #     heapq.heappush(Q,[c,n])
   # else:
   P[idx] = n
   D[n] = idx
   idx += 1
   lst[X[n-1]][1] -= C[n-1]
   heapq.heappush(Q,(lst[X[n-1]][1], X[n-1]))
   done[n] = True


pass
# D = dict()
# for i,(n,_) in enumerate(lst):
#     P[i] = n
#     D[n] = i

ans = 0
for i, x in enumerate(X,start=1):
    if D[i] > D[x]:
        ans += C[i-1]
print(ans)