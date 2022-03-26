def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))
import sys
sys.setrecursionlimit(10000000)


N = II()
S = I()
ans = 0
for i in range(1000):
    num = str(i).zfill(3)

    num_c = 0
    for s in S:
        if s == num[num_c]:
            num_c += 1
            if num_c == 3:
                ans += 1
                break

print(ans)