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

#解説AC

N = II()
A = LIIS()
Am = min(A)

#桁数
digit = N//Am

ans = []
cost = N
for n in range(digit):
    for i in range(9,0,-1):
        if (digit-n-1) * Am <= cost - A[i-1] < (digit-n) * Am:
            cost -= A[i-1]
            ans.append(str(i))
            break
print(''.join(ans))

# t = 0
# tt = INF
# for i,a in enumerate(A,start=1):
#     if tt >= a:
#         t = i
#         tt = a
#
# ans = [str(t)] * (digit-1)
#
# #残りのコスト
# m = min(A) + N%min(A)
#
# ttt = 0
# for i, a in enumerate(A,start=1):
#     if a > m:
#         continue
#     ttt = i
#
# ans.append(str(i))
#
# ans.sort(reverse=True)

# print(''.join(ans))