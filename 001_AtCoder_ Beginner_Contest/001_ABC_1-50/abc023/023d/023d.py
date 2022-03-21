def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)


N = II()
HS = [LIIS() for _ in range(N)]

ok = 10 ** 9 + ((10 ** 9) * 100000) + 1
ng = 0

def check(n):
    # n点以内にすべての風船を割れるか
    times = []
    for h, s in HS:
        if h > n:
            return False

        t = (n-h) // s  # t回以内に割る必要がある
        times.append(t)

    times.sort()

    for i,time in enumerate(times):
        if i > time:    #iは現在の回数 timeはi回目までに割らなければならない制限時間
            return False

    return True

while abs(ok-ng)>1:
    mid = (ng+ok) // 2

    if check(mid):
        ok = mid
    else:
        ng = mid

print(ok)