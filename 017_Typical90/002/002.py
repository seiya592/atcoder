def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)


N = II()
if N % 2 == 1:
    print('')
    exit()

N = N // 2

dp = [[] for _ in range(N+1)]

dp[0].append('')

for i in range(1,N+1):
    # # ()を追加する
    # for d in dp[i-1]:
    #     dp[i].append(d+'()')
    #     dp[i].append('()'+d)
    #
    # # i%2が奇数か偶数かで処理が変わる？
    # if i > 1:
    #     if i % 2 == 0:
    #         for d in dp[i//2]:
    #             for p in dp[i//2]:
    #                 dp[i].append(f'{d}{p}')
    #                 dp[i].append(f'{p}{d}')
    #     else:
    #         for d in dp[i//2]:
    #             for p in dp[i//2 + 1]:
    #                 dp[i].append(f'{d}{p}')
    #                 dp[i].append(f'{p}{d}')
    for j in range(1,i):
        for k in range(1,i):
            if j+k == i:
                for d in dp[j]:
                    for p in dp[k]:
                        dp[i].append(f'{d}{p}')
                        dp[i].append(f'{p}{d}')

    # ()で囲む
    for d in dp[i-1]:
        dp[i].append(f'({d})')

    dp[i] = list(set(dp[i]))

dp[N].sort()
for d in dp[N]:
    print(d)


