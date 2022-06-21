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
# dpである値を除いた値をO(NK)で作って間に合う（最大11回= O(NKlogN)）ことがわかった
# なんとなく単調性があることはわかったが解説で確信に変わった
# 要素外アクセス気を付ける（aの値が極端に大きいときにDPの配列をそこまで用意していない）


N, K = IIS()
A = LIIS()



A.sort()
ok = -1  #不要なカードの枚数
ng = N  #必要なカードの枚数

def calc(n):
    dp = [False] * (K + 1)
    dp[0] = True
    for i, a in enumerate(A):
        if i == n:
            continue
        for i in range(K, a - 1, -1):
            dp[i] = dp[i - a] | dp[i]

    #K以上の値は単体で絶対必要な集合になる
    if K <= A[n]:
        return True

    # A[n]をある集合に入れるとK未満の値がK以上になる場合はNG（True）
    for i in range(K-A[n],K):
        if dp[i]:
            #このnが必要な集合が１つでも存在する
            return True
    return False

while abs(ok - ng) > 1:
    mid = (ok+ng) // 2
    if calc(mid):
        ng = mid
    else:
        ok = mid
print(ok+1)