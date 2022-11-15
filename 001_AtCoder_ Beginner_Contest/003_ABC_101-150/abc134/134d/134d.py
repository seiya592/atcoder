"""
2022/11/15 19:46:19
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
def CEIL(x,y): return -(-x // y)    # 除算を小数点切り上げ
import sys
sys.setrecursionlimit(500000)
INF = 10**17


N = II()
A = LIIS()
ans = []
num = [0] * (N+1)
for i in reversed(range(1,N+1)):
    t = 0
    for j in range(i,N+1,i):
        t ^= num[j-1]
    if t != A[i-1]:
        num[i-1] = 1
        ans.append(i)
print(len(ans))
if ans:
    print(*ans)