"""
2022/11/12 20:42:20
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

# 参考 https://note.nkmk.me/python-union-find/

from collections import defaultdict
class UnionFind():
    def __init__(self, n):
        """
        parent[i] : i番目の親 , 根の場合は負数(絶対値はその根の持つ要素数)
        :param n: 要素数
        """
        self.n = n                  # 要素数
        self.parents = [-1] * n

    def find(self, x):
        """
        要素xが属するグループの根の要素番号を返す
        :return:int xの根の要素番号
        """
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        """
        要素xが属するグループと要素yが属するグループとを併合する
        """
        x = self.find(x)        # 要素xの根
        y = self.find(y)        # 要素yの根
        if x == y:
            return

        # Union by Size
        # サイズが大きいほうに小さいほうを加える
        if self.parents[x] > self.parents[y]:   # サイズが負数で格納されているため、この場合yのほうが大きい場合
            x, y = y, x     # xとy入れ替え

        # xが大きい状態
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        """
        要素xが属するグループのサイズ（要素数）を返す
        """
        return -self.parents[self.find(x)]  # 負数で管理している為　-付ける

    def same(self, x, y):
        """
        要素x, yが同じグループに属するかどうかを返す
        :return:True→同じグループ
        """
        return self.find(x) == self.find(y)

    def members(self, x):
        """
        要素xが属するグループに属する要素をリストで返す
        O(NlogN)
        """
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        """
        すべての根の要素をリストで返す
        O(n)
        """
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        """
        グループの数を返す　0が使われない頂点の場合0が孤立した根になっていることに注意！！！！
        O(n)
        """
        return len(self.roots())

    def all_group_members(self):
        """
        {ルート要素: [そのグループに含まれる要素のリスト], ...}のdefaultdictを返す
        O(NlogN)
        """
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        """
        print()での表示用
        ルート要素: [そのグループに含まれる要素のリスト]を文字列で返す
        O(NlogN)
        """
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())


# 上のクラスを文字列やタプルなどでも使えるように
# 上のと比べてInitのオーダーが辞書を作成する為が3倍　n=4,000,000付近で2s超えるので注意！！！！
class UnionFindLabel(UnionFind):
    def __init__(self, labels):
        """
        parent[i] : i番目の親の要素番号 , 根の場合は負数(絶対値はその根の持つ要素数)
        d[labelsの要素]: 割り当てられた要素番号
        d_inv[割り当てられた要素番号]: labelsの要素
        :param labels: リスト型(一応文字列でも) 要素は辞書のキーとして使えるオブジェクト str/int/tupleなど listはNG
        """
        assert len(labels) == len(set(labels))      # リスト(labels)の中に同じ要素があった場合エラー

        self.n = len(labels)                                # 要素数
        self.parents = [-1] * self.n
        self.d = {x: i for i, x in enumerate(labels)}
        self.d_inv = {i: x for i, x in enumerate(labels)}

    def find_label(self, x):
        """
        :param x: labelsの要素
        :return: labels要素xが属するグループの根のlabelsの要素を返す
        find が様々な場所で使っているのでオーバーライドできない為別名で定義
        """
        return self.d_inv[super().find(self.d[x])]

    def union(self, x, y):
        """
        labels要素xが属するグループとlabels要素yが属するグループとを併合する
        """
        super().union(self.d[x], self.d[y])

    def size(self, x):
        """
        labels要素xが属するグループのサイズ（要素数）を返す
        :param x:
        :return:
        """
        return super().size(self.d[x])

    def same(self, x, y):
        """
        labels要素x, labels要素yが同じグループに属するかどうかを返す
        :return:True→同じグループ
        """
        return super().same(self.d[x], self.d[y])

    def members(self, x):
        """
        labels要素xが属するグループに属するlabels要素をリストで返す
        O(NlogN)
        """
        root = self.find(self.d[x])
        return [self.d_inv[i] for i in range(self.n) if self.find(i) == root]

    def roots(self):
        """
        すべての根のlabels要素をリストで返す
        O(n)
        """
        return [self.d_inv[i] for i, x in enumerate(self.parents) if x < 0]

    def all_group_members(self):
        """
        {labelsルート要素: [そのグループに含まれるlabels要素のリスト], ...}のdefaultdictを返す
        O(NlogN)
        """
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.d_inv[self.find(member)]].append(self.d_inv[member])
        return group_members

# N,M = IIS()
# A = LIIS()
# UF = UnionFind(N)
# # UF
# # UF = UnionFindLabel(A)
#
# # 同じグループに属せるのは？
# # MODをあらかじめ取っておく
#
# IBM = []
# IB = []
# for i in range(N):
#     IBM.append((A[i]%M, i))
#     IB.append((A[i], i))
#
# # ソート
# IB.sort(key=lambda x:x[0])
# IBM.sort(key=lambda x:x[0])
#
# # +1または同じなら辺を張れる
# old = -INF
# old_i = -1
#
#
#
# for i in range(N):
#     n,i = IBM[i]
#     if n == old + 1:
#         UF.union(i,old_i)
#
#     if n == 0 and old_i == (M-1):
#         UF.union(i,old_i)
#
#     old = n
#     old_i = i
#
# old = -INF
# old_i = -1
# for i in range(N):
#     n,i = IB[i]
#     if n == old:
#         UF.union(i,old_i)
#     old = n
#     old_i = i
#
# ans_t = sum(A)
# ans = INF
#
# for m in UF.all_group_members().values():
#     tmp = 0
#     for z in m:
#         tmp += A[z]
#     ans = min(ans, ans_t-tmp)
# print(ans)
#
#
# #同じ数はまとめていい
# #まとめたらMODの階段数が減るからダメ

N,M = IIS()
A = LIIS()
B = []
for i,a in enumerate(A):
    B.append((a,i))
import collections
MOD_V = collections.defaultdict(list)

for i,a in enumerate(A):
    MOD_V[a%M].append((a,i))

MOD_V = dict(MOD_V)
for k in MOD_V.keys():
    MOD_V[k].sort(key=lambda x:-x[0])


dist = [-INF] * (N+1)

def dfs(n,d):
    if dist[n] != -INF:
        return dist[n]



for i in range(N):
    dfs(i,0)