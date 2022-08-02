def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
def LI(n): return [I() for _ in range(n)]
def PLUS(x,y): return [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]
def YES(): print('Yes'), exit()
def NO(): print('No'), exit()
import sys
sys.setrecursionlimit(500000)
INF = 10**10
def factorization(n):
    arr = 0
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr += cnt

    if temp!=1:
        arr += 1

    if arr==[]:
        arr += 1

    return arr


N = II()
ans = [0] * (N+1)
ans[1] = 1


for i in range(2,N+1):
    if ans[i]:
        continue
    now = factorization(i) + 1
    ans[i] = now
    now += 1
    t = 1
    # while i * 2**t <= N:
    #     ans[i*2**t] = now
    #     now += 1
    #     t +=1
print(*ans[1:])