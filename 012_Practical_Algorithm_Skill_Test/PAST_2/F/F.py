def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)


N = II()
Day = [[] for _ in range(N)]   # i日後から可能になるタスクのポイントを格納

for _ in range(N):
    a,b = IIS()
    Day[a-1].append(b)

task = [0] * 101 # その日に可能なタスクでiポイントのタスクがいくつあるか 最大100
ans = 0
for i in range(N):
    #可能なタスク整理
    for d in Day[i]:
        task[d] += 1

    for j in range(100,0,-1):
        if task[j] > 0:
            task[j] -= 1
            ans += j
            break

    print(ans)


