def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
import sys
sys.setrecursionlimit(10000000)
from collections import deque


Q = II()
Query = LLIIS(Q)

dq = deque()

for q in Query:
    if q[0] == 1:
        dq.append([q[1], q[2]]) #[num / count]
    if q[0] == 2:
        c = q[1]
        ans = 0
        while c > 0:
            num, count = dq.popleft()
            if c < count:
                ans += c * num
                dq.appendleft([num, count-c])
                c = 0
            else:   # 足りない場合
                ans += count * num
                c -= count
        print(ans)


