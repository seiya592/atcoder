def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)


N = II()
dist_1_to_n = [-1] * (N + 1)
dist_1_to_n[1] = 0
for i in range(2, N+1):

    # 問い合わせる
    print(f'? {1} {i}')
    sys.stdout.flush()
    dist = II()
    dist_1_to_n[i] = dist

# 最大値の頂点を求める
max_index = dist_1_to_n.index(max(dist_1_to_n))
dist_max_to_n = [-1] * (N+1)
dist_max_to_n[max_index] = 0
for i in range(1, N+1):

    if max_index != i:
        # 問い合わせる
        print(f'? {max_index} {i}')
        sys.stdout.flush()
        dist = II()
        dist_max_to_n[i] = dist

print(f'! {max(dist_max_to_n)}')