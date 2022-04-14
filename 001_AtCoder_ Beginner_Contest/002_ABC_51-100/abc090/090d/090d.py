def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(10000000)

# 解説AC

N, K = IIS()
ans = 0
for i in range(K+1,N+1):    # bを固定
    t = N // i       # 割った周期分0→1→2→...i-1 の余りが繰り返される
    t2 = max(0,(i-1) - (K-1))   # i-1の周期 3=(0→1→2)から K=2以上を抽出
    ans += t * t2   #割り切れる数で最低限繰り返される
    ans += max(0, (N % i) - (K-1))    #割った周期の余りの分を考慮

if K == 0:
    ans -= N    # 組み合わせの最小値は1だが、計算時に0も含めてカウントしている。　余り0が対象なら足しすぎている分を引く
print(ans)