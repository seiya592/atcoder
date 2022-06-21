def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)


N, A, B, C = IIS()
L = []
for _ in range(N):
    l = II()
    L.append(l)

flg = [0] * N   #どの竹を使うか０～３

def dfs(i):
    global ans
    if i != N:
        # 今の番号の竹をどの材料に使うかフラグ立てて、次の竹をセットする　全探索で全パターン試す
        for n in range(4):
            flg[i] = n  # フラグをセット 0→Aに使用 1→Bに使用 2→Cに使用 3→使用しない
            dfs(i+1)
    else:
        # すべての竹のフラグセット完了

        # 各材料どの竹を使うか確認
        cost = 0
        le = [0] * 4
        for i, f in enumerate(flg):
            if f != 3 and le[f] != 0:
                # 合成魔法を使用したならコストを払う
                cost += 10
                le[f] += L[i]
            else:
                #初回　or 合成魔法ではない何もしないに足した場合
                le[f] = L[i]

        for le2 in le[:3]:
            if not le2:
                # 無から魔法は使えないのでありえない組み合わせとして終了する
                return

        # 合成魔法終了 ここから伸縮魔法で条件に満たすようにMPを使用する
        cost += abs(le[0] - A) + abs(le[1] - B) + abs(le[2] - C)
        if cost == 120:
            pass
        ans = min(ans, cost)

ans = 10**100

dfs(0)
print(ans)