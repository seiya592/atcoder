import string


def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)


# 解説AC

N, K = IIS()
S = I()

# 解説部分nex作成
nex = [{} for _ in range(N)]
# nex[i文字目]{key='a-z':value=i文字目から見て最短で何番目に存在するか}

# init
for s in string.ascii_lowercase:
    nex[N-1][s] = -1
nex[N-1][S[N-1]] = 0

# 後ろから詰めていく
for i in reversed(range(N-1)):
    for a in string.ascii_lowercase:
        if S[i] == a:
            nex[i][a] = 0
        else:
            nex[i][a] = nex[i+1][a] + 1 if nex[i+1][a] != -1 else -1



# 貪欲法
# 先頭になりえる文字列でaに近い文字を探していく
ans = ''
k = K
now = 0
while True:
    for a in string.ascii_lowercase:
        if nex[now][a] != -1 and N - (nex[now][a] + now) >= k:
            ans += a
            k -= 1
            now += nex[now][a] + 1
            break
    if k <= 0:
        break
print(ans)