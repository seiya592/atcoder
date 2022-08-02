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


S = I()
S = ''.join(list(reversed(S)))
MOD=2019
# 各桁の合計を2019で割った累積和を作る
T = [0] * (len(S)+1)

x = 1   # 10のx乗
for i,s in enumerate(S):
    T[i+1] = T[i] + (int(s) * x)
    T[i+1] %= MOD

    x = (10 * x) % MOD    # ここでMODをとらなくても計算は成り立つが、xの数が大きくなるのでここでも割っておく

# 累積和をそれぞれカウント
C = [0] * MOD
for t in T:
    C[t] += 1

ans = 0
for c in C:
    # 2019で割った数が同じ場合その区間が2019の倍数で割り切れることになる
    # cC2で求める
    ans += c * (c-1) // 2 * 1
print(ans)