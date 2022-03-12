def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
from collections import deque


K = II()
Q = deque()

for i in range(1,10):
    Q.append(i)

cnt = 0
while True:
    num = Q.popleft()
    cnt += 1

    if K == cnt:
        print(num)
        exit()

    for i in [num % 10 - 1, num % 10, num % 10 + 1]:
        if 0 <= i <= 9:
            tmp = num * 10 + i
            Q.append(tmp)