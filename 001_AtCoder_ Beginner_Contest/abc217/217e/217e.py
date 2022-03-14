def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)
import collections
import bisect
import heapq

Q = II()
Query = [LIIS() for _ in range(Q)]
A = []
heapq.heapify(A)
tmpA = collections.deque()

for q in Query:
    if q[0] == 1:
        tmpA.append(q[1])
    elif q[0] == 2:
        if len(A):
            print(heapq.heappop(A))
        else:
            print(tmpA.popleft())
    else:
        for i in range(len(tmpA)):
            heapq.heappush(A,tmpA.popleft())
