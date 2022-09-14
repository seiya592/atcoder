"""
2022/09/14 17:36:50
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


S = I()
N = len(S)

if N == 2:
    if S[0] == S[1]:
        print(1,2)
    else:
        print(-1,-1)
    exit()

for i in range(N-2):
    s1 = S[i]
    s2 = S[i+1]
    s3 = S[i+2]

    if s1 == s2 or s2 == s3 or s1 == s3:
        print(i+1, i+3)
        exit()
print(-1,-1)