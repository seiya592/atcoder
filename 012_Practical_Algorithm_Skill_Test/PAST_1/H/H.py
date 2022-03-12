def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import math

N = II()
C = LIIS()
Q = II()
S = [LIIS() for _ in range(Q)]

odd_min = min(C[::2])
if N == 1:
    even_min = 10000000000000000000000
else:
    even_min = min(C[1::2])

ans = 0
s_cnt = 0
ss_cnt = 0

for s in S:
    if s[0] == 1:
        x = s[1]
        a = s[2]
        if x % 2 == 1:
            if (C[x - 1] - ss_cnt) - s_cnt < a:
                continue
        else:
            if C[x - 1] - ss_cnt < a:
                continue

        C[x-1] -= a
        ans += a
        if x % 2 != 1:
            even_min = min(even_min, C[x-1])
        else:
            odd_min = min(odd_min, C[x-1])

    elif s[0] == 2:
        a = s[1]
        if odd_min - s_cnt - ss_cnt >= a:
            s_cnt += a
    else:
        a = s[1]
        if min(even_min, odd_min - s_cnt) - ss_cnt >= a:
            ss_cnt += a

ans += N * ss_cnt
ans += s_cnt * math.ceil(N / 2)

print(ans)