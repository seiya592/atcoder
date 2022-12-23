"""
2022/12/08 22:31:00
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

D = [0,1,3,6,10,15,21,28,36,45]

N = II()
digit = 0
ans = 0
done = 0
while N:
    n = N % 10
    N = N // 10

    ans += 45 * N * (10 ** digit) + D[max(n-1,0)] * (10 ** digit) + n * (done + 1)

    done += n * 10 ** digit
    digit += 1
print(ans)