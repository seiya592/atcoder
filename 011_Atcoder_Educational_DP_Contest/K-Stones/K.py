"""
2022/09/24 23:40:17
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


N,K = IIS()
A = LIIS()
dp = [False] * (K+1)
# dp[残りの山の数がn個] = の時の手番プレイヤーが勝てるかどうか
# 全てのn-aを見て1つでも負けの数に遷移できるならそこに移動させれれば勝てるので 山nを担当したプレイヤーは勝ち
# 逆にどこに遷移しても負けならその山nを担当したプレイヤーは負け

# 貰うdp
for n in range(1, K+1):
    t = True
    for a in A:
        if n-a < 0:
            continue
        t &= dp[n-a]    # 1つでも負けがあればtはFalseになる = この山の残数プレイヤーは勝ちになる

    dp[n] = (t == False)


if dp[K]:
    print('First')
else:
    print('Second')