"""
2022/09/10 20:45:46
"""
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
INF = 10**17


N = II()
P = LIIS()


#喜ばれる回転数
#CNT[回転数] =喜ぶ人
CNT = [0] * (N+1)

for i,p in enumerate(P):
    CNT[(N+(p-1)-i)%N] += 1
    CNT[(N + (p)-i) % N] += 1
    CNT[(N + (p + 1)-i) % N] += 1
print(max(CNT))