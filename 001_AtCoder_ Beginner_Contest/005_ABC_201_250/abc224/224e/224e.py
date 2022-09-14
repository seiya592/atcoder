"""
2022/08/30 23:25:09
"""
def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS()+[i] for i in range(n)]
def LI(n): return [I() for _ in range(n)]
def PLUS(x,y): return [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]
def YES(): print('Yes'), exit()
def NO(): print('No'), exit()
import sys
sys.setrecursionlimit(500000)
INF = 10**10


H,W,N = IIS()
RCA = LLIIS(N)
RCA.sort(key=lambda x:x[2], reverse=True)

# R = [[0] for _ in range(H+1)]
# C = [[0] for _ in range(W+1)]

# tR = [[0] for _ in range(H+1)]
# tC = [[0] for _ in range(W+1)]
C = [0] * (W+1)
R = [0] * (H+1)
# tC = [0] * (W+1)
# tR = [0] * (H+1)

ANS = [0] * N
now = RCA[0][2]
start_idx = 0
for now_idx, (r,c,a,i) in enumerate(RCA):
    if now != a:
        while start_idx < now_idx:
            t = ANS[RCA[start_idx][3]]
            R[RCA[start_idx][0]] = max(R[RCA[start_idx][0]], t+1)
            C[RCA[start_idx][1]] = max(C[RCA[start_idx][1]], t+1)
            start_idx += 1
        # R = copy.copy(tR)
        # C = copy.copy(tC)
        now = a

    ans = max(R[r],C[c])
    ANS[i] = ans

    # tR[r] = max(ans + 1,tR[r])
    # tC[c] = max(ans + 1,tC[c])

for a in ANS:
    print(a)