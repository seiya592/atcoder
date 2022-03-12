def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)


def has_bit(n, i):
    return (n & (1<<i)) > 0

N = II()
ALL = 2 ** N    # 考えられるすべての組み合わせ

A = []  # 前半はダミー
for i in range(N - 1):
    A.append([0]*(i+1) + LIIS())

happy = [0] * ALL

# 全探索で全員の幸福度を求める
for n in range(ALL):
    for i in range(N-1):
        for j in range(i+1,N):
            if has_bit(n,i) and has_bit(n,j):
                happy[n] += A[i][j]

ans = -10 ** 100
for i in range(ALL):
    for j in range(ALL):
        if (i & j) > 0: # 積集合でかぶっている場合はありえない組み合わせ
            continue

        k = (ALL-1) - (i | j) # グループi,jに含まれていない３つめのグループ

        ans = max((happy[i] + happy[j] + happy[k]), ans)

print(ans)