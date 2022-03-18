import string


def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)
from collections import deque
from collections import defaultdict

N = II()
Q = deque()
d = {}

for i in range(N):
    q = IS()

    if q[0] == '1':
        Q.append([q[1], int(q[2])])
    else:
        q[1] = int(q[1])
        d = defaultdict(int)

        while len(Q) and q[1] > 0:
            if Q[0][1] <= q[1]:
                c, x = Q.popleft()
                d[c] += x
                q[1] -= x
            else:
                Q[0][1] -= q[1]
                d[Q[0][0]] += q[1]
                q[1] = 0
        ans = 0
        for a in string.ascii_lowercase:
            ans += d[a] ** 2
        print(ans)

