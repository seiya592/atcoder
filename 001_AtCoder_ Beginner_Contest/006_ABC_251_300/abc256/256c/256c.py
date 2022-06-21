def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
def LLIIS(n): return [LIIS() for _ in range(n)]
def LI(n): return [I() for _ in range(n)]
def PLUS(x,y): return [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]
import sys
sys.setrecursionlimit(500000)
INF = 10**10


#4つ値が決まれば一意に値が決まる
H1,H2,H3,W1,W2,W3 = IIS()


#i,j,k
#x,y,z
#a,b,c
ans = 0
for i in range(1,30):
    for j in range(1,30):
        for x in range(1,30):
            for y in range(1,30):
                #H1
                k = H1 - i - j
                if k <= 0:
                    continue

                #H2
                z = H2 - x - y
                if z <= 0:
                    continue

                a = W1 - i - x
                if a <= 0:
                    continue

                b = W2 - j - y
                if b <= 0:
                    continue

                c1 = W3 - k - z
                c2 = H3-a-b
                if c1 == c2 and c1 > 0:
                    ans += 1
                else:
                    continue
print(ans)