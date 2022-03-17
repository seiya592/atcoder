def I(): return input().rstrip()
def IS(): return input().split()
def II(): return int(input())
def IIS(): return map(int, input().split())
def LIIS(): return list(map(int, input().split()))


import sys
sys.setrecursionlimit(10000000)
ans = 0

N = II()


def dfs(num):
    global N
    global ans
    st = str(num)
    if st.find('3') >= 0 and st.find('5') >= 0 and st.find('7') >= 0:
        ans += 1
    tmp = num * 10
    for t in [tmp + 3, tmp + 5 , tmp +7]:
        if t <= N:
            dfs(t)


dfs(0)
print(ans)