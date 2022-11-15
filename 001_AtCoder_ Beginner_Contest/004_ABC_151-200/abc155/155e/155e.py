"""
2022/10/03 17:50:52
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


N = I()

# dpだけど1つ前の状態だけ保持していればOKなので配列は作らない

old_pay_1 = 0
old_pay_2 = 1
now_pay_1 = 0
now_pay_2 = 0
# 1…対象の桁の金額分のお札を出しておつりを0にする
# 2…対象の桁の金額分のお札は出さずに、１つ繰り上がった桁で1枚余分にお札を出しておつりを受け取る

for n in reversed(N):
    n = int(n)

    # この桁のお札を全て出す
    now_pay_1 = min(old_pay_1 + n, old_pay_2 + n + 1)

    # この桁のお札を出さずに繰り上げておつりを貰う
    now_pay_2 = min(old_pay_1 + (10-n), old_pay_2 + (10 - (n + 1)))

    old_pay_1 = now_pay_1
    old_pay_2 = now_pay_2

print(min(old_pay_1, old_pay_2+1))